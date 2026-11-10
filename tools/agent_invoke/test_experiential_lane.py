"""Offline checks for outbound data and credit-spending boundaries."""
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

import experiential_lane as lane


class LaneTests(unittest.TestCase):
    def run_lane(self, argv, response=None, error=None):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.dict(os.environ, {"EXPLABS_API_KEY": "test-secret"}, clear=True), \
                patch.object(lane, "request", return_value=(response, "request-1"), side_effect=error) as request, \
                contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                status = lane.main(argv)
            except SystemExit as exc:
                status = exc.code
        return status, stdout.getvalue(), stderr.getvalue(), request

    def test_private_input_refused_before_network(self):
        status, _, _, request = self.run_lane(["sensitive input"])
        self.assertNotEqual(status, 0)
        request.assert_not_called()

    def test_paid_and_fable_models_refused_before_network(self):
        for model in ["claude-fable-5.1", "deepseek-v4.1-flash", "gpt-6-luna:free"]:
            with self.subTest(model=model):
                status, _, _, request = self.run_lane(["ok", "--public", "--model", model])
                self.assertNotEqual(status, 0)
                request.assert_not_called()

    def test_invalid_token_limits_refused_before_network(self):
        for limit in ["0", "-1", "16001"]:
            status, _, _, request = self.run_lane(["ok", "--public", "--max-tokens", limit])
            self.assertNotEqual(status, 0)
            request.assert_not_called()

    def test_free_suffix_one_attempt_no_fallback_and_zero_cost(self):
        data = {"model": "deepseek-v4.1-flash", "provider": "experiential_cloud",
                "usage": {"cost": 0}, "choices": [{"message": {"content": "OK"}}]}
        status, stdout, _, request = self.run_lane(["ok", "--public"], data)
        self.assertEqual(status, 0)
        self.assertEqual(stdout, "OK\n")
        request.assert_called_once()
        body = request.call_args.args[2]
        self.assertEqual(body["model"], "deepseek-v4.1-flash:free")
        self.assertEqual(body["gateway"]["retry"]["max_total_attempts"], 1)
        self.assertFalse(body["gateway"]["routing"]["allow_fallbacks"])

    def test_missing_nonzero_or_invalid_cost_withholds_answer(self):
        for usage in [{}, {"cost": None}, {"cost": "0.01"}, {"cost": "NaN"}, {"cost": "invalid"}]:
            data = {"model": "deepseek-v4.1-flash", "usage": usage,
                    "choices": [{"message": {"content": "unconfirmed answer"}}]}
            status, stdout, _, request = self.run_lane(["ok", "--public"], data)
            self.assertNotEqual(status, 0)
            self.assertEqual(stdout, "")
            request.assert_called_once()

    def test_unexpected_model_withholds_answer(self):
        data = {"model": "claude-fable-5.1", "usage": {"cost": 0},
                "choices": [{"message": {"content": "wrong model"}}]}
        status, stdout, _, _ = self.run_lane(["ok", "--public"], data)
        self.assertNotEqual(status, 0)
        self.assertEqual(stdout, "")

    def test_network_failure_does_not_retry_and_redacts_key(self):
        status, stdout, stderr, request = self.run_lane(["ok", "--public"], error=RuntimeError("test-secret"))
        self.assertNotEqual(status, 0)
        self.assertEqual(stdout, "")
        self.assertNotIn("test-secret", stderr)
        request.assert_called_once()

    def test_legacy_secret_spelling_and_content_free_log(self):
        with tempfile.TemporaryDirectory() as directory:
            env_file, log = Path(directory) / "secrets.env", Path(directory) / "usage.jsonl"
            env_file.write_text("export EXPERIMENTAL_LABS_API_KEY='test-key' # local\n")
            with patch.dict(os.environ, {"EXPLABS_SECRETS_FILE": str(env_file), "EXPLABS_USAGE_LOG": str(log)}, clear=True):
                self.assertEqual(lane.load_key(), "test-key")
                lane.log_usage({"requested_model": lane.MODEL, "cost_usd": 0})
                self.assertEqual(json.loads(log.read_text())["cost_usd"], 0)
                self.assertNotIn("test-key", log.read_text())

    def test_redirect_cannot_forward_authorisation(self):
        request = lane.urllib.request.Request(lane.BASE_URL + "/v1/models", headers={"Authorization": "Bearer test-secret"})
        handler = lane.NoRedirect()
        self.assertIsNone(handler.redirect_request(request, None, 302, "Found", {}, "https://other.example/collect"))
        with patch.object(lane.urllib.request, "build_opener") as build:
            response = build.return_value.open.return_value.__enter__.return_value
            response.read.return_value = b'{}'
            response.headers = {}
            lane.request("/v1/models", "test-secret")
            self.assertIsInstance(build.call_args.args[0], lane.NoRedirect)

    def test_usage_log_failure_does_not_raise_or_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            stderr = io.StringIO()
            with patch.dict(os.environ, {"EXPLABS_USAGE_LOG": directory}, clear=True), contextlib.redirect_stderr(stderr):
                lane.log_usage({"ok": True, "cost_usd": 0})
            self.assertIn("usage log unavailable", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()

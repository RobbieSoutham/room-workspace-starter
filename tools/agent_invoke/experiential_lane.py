#!/usr/bin/env python3
"""Explicit Experiential Labs free lane for public, non-sensitive text.

Uses the documented :free suffix: quota exhaustion must not spend credits.
Supply EXPLABS_API_KEY, or point EXPLABS_SECRETS_FILE at an untracked env file.
The existing EXPERIMENTAL_LABS_API_KEY spelling is also supported.
"""
import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import json
import os
from pathlib import Path
import shlex
import sys
import urllib.error
import urllib.request

BASE_URL = "https://api.experientiallabs.ai"
MODEL = "deepseek-v4.1-flash:free"
KEY_NAMES = ("EXPLABS_API_KEY", "EXPERIMENTAL_LABS_API_KEY")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # The API host is fixed; never forward a credential through a redirect.
        return None


def load_key():
    for name in KEY_NAMES:
        if os.environ.get(name):
            return os.environ[name]
    path = os.environ.get("EXPLABS_SECRETS_FILE")
    if path:
        for line in Path(path).read_text().splitlines():
            name, sep, value = line.strip().removeprefix("export ").partition("=")
            if sep and name.strip() in KEY_NAMES:
                words = shlex.split(value, comments=True)
                if words:
                    return words[0]
    raise ValueError("Set EXPLABS_API_KEY or EXPLABS_SECRETS_FILE; the key is never printed")


def request(path, key, body=None):
    req = urllib.request.Request(BASE_URL + path,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json",
                 "User-Agent": "room-workspace-experiential/1.0"})
    try:
        with urllib.request.build_opener(NoRedirect()).open(req, timeout=60) as response:
            return json.load(response), response.headers.get("x-request-id")
    except urllib.error.HTTPError as exc:
        # Error bodies can echo input. Report structured codes only.
        try:
            detail = json.loads(exc.read(65536)).get("error", {})
            code = detail.get("code", "provider_error") if isinstance(detail, dict) else "provider_error"
        except (ValueError, AttributeError):
            code = "provider_error"
        raise RuntimeError(f"HTTP {exc.code}: {str(code).replace(key, '[REDACTED]')}; no retry or paid fallback") from None


def log_usage(record):
    path = os.environ.get("EXPLABS_USAGE_LOG")
    if path:
        try:
            target = Path(path)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("a") as output:
                output.write(json.dumps(record) + "\n")
        except OSError as exc:
            print(f"experiential: usage log unavailable ({type(exc).__name__}); call is not retried", file=sys.stderr)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", help="public text, or - for stdin")
    parser.add_argument("--public", action="store_true", help="confirm public, non-sensitive input")
    parser.add_argument("--model", choices=[MODEL], default=MODEL)
    parser.add_argument("--max-tokens", type=int, default=1500)
    parser.add_argument("--check", action="store_true", help="read-only key and balance check; no inference")
    args = parser.parse_args(argv)
    if not args.check and (not args.public or args.prompt is None):
        parser.error("inference requires a prompt and --public")
    if not 1 <= args.max_tokens <= 16000:
        parser.error("--max-tokens must be between 1 and 16000")
    record = {"ts": datetime.now(timezone.utc).isoformat(), "requested_model": args.model, "ok": False}
    key = ""
    try:
        key = load_key()
        if args.check:
            info, _ = request("/api/v1/key", key)
            wallet, _ = request("/api/v1/credits", key)
            balance = Decimal(str(wallet["data"]["total_credits"])) - Decimal(str(wallet["data"]["total_usage"]))
            print(json.dumps({"key_valid": True, "is_free_tier": info["data"].get("is_free_tier"),
                              "balance_usd": str(balance), "balance_credits": str(balance * 100)}))
            return 0
        prompt = sys.stdin.read() if args.prompt == "-" else args.prompt
        data, request_id = request("/v1/chat/completions", key, {
            "model": args.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": args.max_tokens,
            "reasoning_effort": "none",
            "gateway": {"retry": {"max_attempts_per_route": 1, "max_total_attempts": 1},
                        "routing": {"allow_fallbacks": False}},
        })
        usage = data.get("usage") or {}
        record.update({"request_id": request_id, "returned_model": data.get("model"),
                       "provider": data.get("provider"), "cost_usd": usage.get("cost"),
                       "prompt_tokens": usage.get("prompt_tokens"),
                       "completion_tokens": usage.get("completion_tokens")})
        if usage.get("cost") is None or Decimal(str(usage["cost"])) != 0:
            raise RuntimeError("free response did not confirm usage.cost=0; inspect request cost before further calls")
        if data.get("model") not in (MODEL, MODEL.removesuffix(":free")):
            raise RuntimeError("unexpected returned model; inspect the request before further calls")
        content = data["choices"][0]["message"].get("content")
        if not isinstance(content, str) or not content.strip():
            raise RuntimeError("empty answer; no retry or paid fallback")
        record["ok"] = True
        log_usage(record)
        print(f"experiential: {record['returned_model']}; cost USD 0; request {request_id}", file=sys.stderr)
        print(content.strip())
        return 0
    except (OSError, ValueError, KeyError, IndexError, TypeError, AttributeError, RuntimeError, InvalidOperation) as exc:
        message = str(exc).replace(key, "[REDACTED]") if key else str(exc)
        record["error"] = message
        log_usage(record)
        print("experiential: " + message, file=sys.stderr)
        return 75


if __name__ == "__main__":
    sys.exit(main())

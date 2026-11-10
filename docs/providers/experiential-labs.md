# Experiential Labs setup

Reviewed 10 November 2026 against the provider's [pricing](https://www.experientiallabs.ai/pricing), [machine reference](https://platform.experientiallabs.ai/llms.txt), [routing controls](https://platform.experientiallabs.ai/docs/waterfall) and [Cost API](https://platform.experientiallabs.ai/docs/cost-api). This guide describes the integration, not any individual's entitlement or balance.

## Access and cost

The canonical serving base is `https://api.experientiallabs.ai/v1`, authenticated with `Authorization: Bearer <key>`. Read-only account/cost endpoints use `/api/v1`. A model appearing in authenticated `/v1/models` is discovery evidence; it does not prove free access or successful inference.

Free core includes GPT-6 Luna, DeepSeek V4.1 Flash and the Clef decision endpoint after card/payment verification, sharing 1M input and output tokens/day with a 00:00 UTC reset. The pricing page describes shared limits of 10 RPM/250K TPM, while the machine reference says per model. Use the conservative shared limit and honour the gateway's 429 response. Legacy accounts may also include Jev; do not assume eligibility from this guide.

Use `deepseek-v4.1-flash:free` for this lane. The documented `:free` suffix stops at free limits and refuses models without an eligible free tier. A plain model slug can overflow onto credits depending on account settings. This client never falls back to a plain slug, changes billing settings or retries a failed request.

One credit is $0.01. The balance API's `total_credits` and `total_usage` are already USD: subtract them for the dollar balance, then multiply by 100 for credits. A credit grant is a finite wallet, separate from any daily free allowance. Claude Fable 5.1 is listed at $10/M input and $50/M output on Free, and is not a free-core model. The workspace's Fable prohibition applies to this provider too.

## Configure and run

Use Python 3.9 or later; only the standard library is needed. Set `EXPLABS_API_KEY` in your private environment, or copy [the blank example](../../config/ai/experiential.env.example) to an untracked private file and set `EXPLABS_SECRETS_FILE` to its path. The older `EXPERIMENTAL_LABS_API_KEY` variable is accepted for compatibility. Keep the actual key outside Git and command-line arguments.

```bash
python3 tools/agent_invoke/experiential_lane.py --check
python3 tools/agent_invoke/experiential_lane.py 'Summarise this public text: ...' --public
cat public.txt | python3 tools/agent_invoke/experiential_lane.py - --public --max-tokens 800
python3 -m unittest discover -s tools/agent_invoke -p test_experiential_lane.py
```

`--check` only reads key metadata and balance. Inference requires `--public` and only accepts `deepseek-v4.1-flash:free`. Every request caps gateway generation at one attempt and disables provider fallback. HTTP redirects are refused to prevent forwarding credentials. An answer must report the expected model and `usage.cost=0`; missing or positive cost stops the client. The cost check is a response check; the provider's `:free` enforcement is the spending boundary.

Set `EXPLABS_USAGE_LOG` to an untracked local JSONL path if you need metadata logging. It records model, serving provider, request ID, cost, token counts and outcome; it does not store the prompt or answer. Log-write failure is reported without repeating inference. The client performs no automatic billing changes, purchases or top-ups.

Use only public, non-sensitive text: the catalogue lists upstream routes with differing training/retention policies. No local files are read except the explicitly configured secret file and stdin. This is an optional low-stakes text lane; transport verification is not a model-quality evaluation. Check the [catalogue](../../config/ai/model_catalog.yaml), [routing policy](../../config/ai/routing_policy.yaml) and [model-evaluation requirements](../model-evaluation-and-benchmarks.md) before promoting its role.

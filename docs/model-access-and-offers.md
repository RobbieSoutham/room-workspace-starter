# Model access, subscriptions and offers

This is the reusable process for comparing model access. Do not copy a particular person's subscriptions, eligibility, account status, usage balances, credentials or provider routing into a shared starter. Live offers change frequently; verify each one at the provider's official source immediately before relying on it.

## Separate the access types

- **Consumer subscription:** bundled access in a chat or coding product. Check usage caps, model availability, fair-use terms, data controls and whether programmatic/API use is excluded.
- **API billing:** metered service attached to an API account/project. Check model prices, context and rate limits, data retention/training terms, region and billing controls. A chat subscription does not automatically include API use.
- **Credits or grants:** promotional or research credits with eligibility, geography, expiry, eligible products, spend caps and potential post-credit charges.
- **Education/research programme:** institution-wide access, student/faculty benefit, research grant or builder programme. Check eligibility, application process, duration, renewal, seat ownership and data terms.
- **Open-weight/local model:** no hosted token bill may still mean hardware, engineering, electricity, licence and operational costs.

Do not compare headline credit value as cash value. Calculate expected usable value against a realistic workload and include setup, overage, renewal and exit costs.

## Offer register

Keep the canonical tracker local to the workspace that owns the access decision. Use one row per programme and record:

| Field | Record |
|---|---|
| Provider/programme | Exact official offer name and product |
| Official source | Direct terms/application URL, not a social post or aggregator |
| Checked | Date last verified; recheck before application or purchase |
| Eligibility | Country, institution, role, new/existing-user rules |
| Value and form | Subscription periods, credits, seats or grant; separate API from chat credit |
| Limits | Expiry, caps, rate limits, eligible models/services, payment method |
| Data and rights | Retention/training terms, research data eligibility and output/use terms |
| Status | `UNVERIFIED`, `ELIGIBLE_TO_APPLY`, `APPLIED`, `ACTIVE`, `EXPIRED`, `INELIGIBLE` |
| Owner/action | Role or team responsible; next review date; no private account identifier |

Keep secrets, claim URLs containing tokens, account emails, verification documents and balances outside Git. The public starter should contain the schema and official-source links only, not a live user's offer status.

## Current offer board

**Last checked against official provider sources: 2026-11-07.** “Open/ongoing” means the provider currently describes an application or claim path; it does not guarantee acceptance, a benefit in every country, or individual eligibility. Rows with an expiry date should be treated as closed after that date unless the provider renews them.

| Provider/programme | Current benefit described by provider | Eligibility and important terms | Status on 2026-11-07 | Official source |
|---|---|---|---|---|
| OpenAI — Codex for Students | $100 ChatGPT credits for Codex use | Verified university students in the US and Canada; one offer/student; credits expire 12 months after grant. These are not API credits. | Claim path listed; geography-limited | [Offer terms](https://developers.openai.com/community/students) |
| OpenAI — ChatGPT for Academic Researchers | Up to five complimentary workspace seats for 12 months, Pro-level rate limits and business data protections | Eligible research faculty or postdocs at participating institutions in supported countries; recent relevant preprint/paper and application required. No API credits; does not auto-renew. | Application path listed; approval required | [Programme and eligibility](https://help.openai.com/en/articles/20001406-chatgpt-for-academic-researchers) |
| OpenAI — Rosalind Academic Plan | Up to 30 complimentary Business Standard seats for 12 months and GPT-Rosalind access | US university labs; PI/lab lead applies; trusted-access approval and biosafety contact; intended for life-sciences discovery. No API credits. | Applications open; approval required | [Current plan terms](https://help.openai.com/en/articles/20001602-rosalind-academic-plan) |
| OpenAI — Researcher Access Program | Up to $1,000 API credit, valid for 12 months | Academic/research organisation or nonprofit research; specifically responsible-AI deployment, risk mitigation and societal-impact work; supported API country. Quarterly review. | Applications accepted year-round; reviewed quarterly | [FAQ and scope](https://help.openai.com/en/articles/10139500-researcher-access-program-faq) |
| OpenAI — complimentary API tokens for data sharing | Eligible organizations may receive daily complimentary tokens on selected shared API traffic; exact models/limits depend on the account's eligibility | Organisation owner must opt in to sharing API inputs and outputs; sensitive, confidential or proprietary data should not be shared. Evals, fine-tuning and tool use are excluded from complimentary-token use. | Conditional; eligibility shown in account settings; not a generally available free tier | [Data-sharing terms](https://help.openai.com/en/articles/10306912-sharing-feedback-evaluation-and-fine-tuning-data-and-api-inputs-and-outputs-with-openai) |
| Anthropic — Claude Team plan for scientists | Standard seats $0/month and Premium seats $15/month for 12 months; includes Team features and Claude Science/Code/Cowork. Scientist Team seats also qualify for monthly API credits ($20 Standard/$100 Premium per seat, subject to the shared cap). | PI/equivalent at an accredited university or nonprofit research institute in natural sciences, mathematics, computer science, engineering and related fields; 1–25 seats; limited availability; verification and approval; renewal at then-current price after 12 months. | Verification/application path listed; limited capacity and approval | [Scientists programme](https://claude.com/programs/team-plan-for-scientists) |
| Anthropic — AI for Science | Up to $20,000 in API credits for six months | Academic/nonprofit research in high-priority scientific areas, with particular emphasis on biology and life sciences; application reviewed on merit; standard model suite only; Usage Policy still applies. | Application path listed; reviewed monthly | [Programme terms](https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program) |
| Anthropic — Max/Ultra/Team monthly API credits | Max: $100/month; Ultra: $200/month; Team: $20 per Standard seat or $100 per Premium seat, pooled up to $500/month. Credits apply to API/agent building, not interactive Claude Code or third-party cloud deployments. | Active eligible paid plan for seven days; link one Console organization; credits expire monthly and are separate from subscription usage. Not available on Free, Pro or Enterprise. | Active plan benefit; not a free subscription | [Credit rules and exclusions](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans) |
| Google — student AI plan | One year of Google AI Pro free for eligible US college students; one year of Google AI Plus free for eligible students in 140+ markets outside the US (market exclusions apply). | Redeem by **2026-12-31**; payment method required; renews at standard local price after trial unless cancelled; student verification required. | Current, deadline approaching | [Google offer and terms](https://blog.google/innovation-and-ai/products/gemini-app/student-offer-google-ai/) |
| Google Cloud — Academic Research Grants | PhD students may apply for up to $1,000/year; faculty/postdocs may apply for one award up to $5,000 | Accredited higher-education/nonprofit research institution in an approved country; proposal, pricing estimate and billing account required; only one applicant per proposal; award discretionary; typical review 6–8 weeks. | Ongoing application | [Application](https://edu.google.com/intl/ALL_us/programs/credits/research/), [eligibility and award rules](https://support.google.com/google-cloud-higher-ed/answer/10724468) |
| AWS — Cloud Credit for Research | Student awards up to $5,000 in AWS Promotional Credit; faculty/staff awards have no stated cap | Accredited research institution; finite research project such as a benchmark, reusable shared tool or workshop (not ongoing general lab operations); rolling review typically 90–120 days; eligible AWS services and expiry terms apply. | Ongoing application | [Programme](https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/), [FAQ](https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/faqs/) |
| Microsoft — Azure for Students | $100 Azure credit for 12 months plus free service allowances | Full-time student, age 18+, eligible degree-granting institution and academic verification; no card at signup; one per eligible customer; credit exhaustion can disable the subscription. Model availability/quota is separate and must be checked. | Available subject to eligibility and supply | [Offer details](https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0170p) |
| Microsoft — Azure for Startups | $1,000 immediately, with up to $5,000 total after business verification | New Azure customers; credits expire after 90 days initially and 180 days post-verification; card required for verification and any usage beyond credits. | Available subject to startup and account eligibility | [Startup/student offers](https://azure.microsoft.com/en-us/free/students/) |
| GitHub — Copilot Student | Free verified-student plan with code completions, GitHub AI Credits and limited chat/agent usage | GitHub Education student verification; eligibility is re-evaluated monthly; model availability and credit limits are set by current plan terms. | Available after verification and activation | [Student setup](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students), [plan comparison](https://docs.github.com/en/copilot/get-started/plans) |

### Free model APIs and compute tiers

These are service tiers rather than grants. Model availability, caps and privacy terms are especially volatile; check the provider dashboard and current model-specific terms before using them. Limits below are provider-published snapshots checked on 2026-11-07.

| Provider/service | Current free access | Limits and cautions | Official source |
|---|---|---|---|
| Google Gemini API / AI Studio | Free API access for selected models; the flagship Gemini 4 Argon is explicitly excluded from the free API tier | Per-model rate limits apply. Google says free-tier content may be used to improve products; do not send confidential, licensed or unpublished research unless the relevant data terms permit it. | [Pricing and free-tier model list](https://ai.google.dev/gemini-api/docs/pricing) |
| Groq API | Free developer tier for supported models | Rate limits vary by model and organization. Current docs list 30 RPM, 1,000 RPD and 200K TPD for `openai/gpt-oss-120b` and `qwen/qwen3.8-27b`; verify the live organization limit page. | [Live model rate limits](https://console.groq.com/docs/rate-limits) |
| OpenRouter Free | Free plan advertises 25+ free models; `openrouter/free` selects a currently available free model | Free model catalog rotates; `:free` endpoints are currently limited to 20 RPM and 50 requests/day, with higher daily caps after a credit purchase. Provider data policies vary; check the actual upstream provider. | [Free models](https://openrouter.ai/collections/free-models), [plan limits](https://openrouter.ai/pricing) |
| Cloudflare Workers AI | 10,000 Neurons/day free allocation | Daily limit resets at 00:00 UTC; some models require a paid Workers plan or prepaid credits. Models and billing units change. | [Pricing and model conditions](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Alibaba Cloud Model Studio new-user quota | Typically 1,000,000 free tokens per eligible model on first activation | Latest quota documentation describes 90-day expiry, real-time inference only, and “Free Quota Only” disabled by default; turn it on to prevent paid overage. Region/deployment scope has changed, so verify model eligibility in the current console before activation. | [Current free quota rules](https://www.alibabacloud.com/help/en/model-studio/new-free-quota) |
| Kaggle Notebooks | Free notebook compute with GPU/TPU accelerators when available | Quota and hardware access are capacity-limited and can vary; current docs describe weekly GPU quotas and queueing, with concurrent-session limits. Not suitable as guaranteed production or unattended compute. | [Notebook setup and free accelerators](https://www.kaggle.com/docs/notebooks), [GPU quota guidance](https://www.kaggle.com/docs/efficient-gpu-usage) |
| Google Colab Free | Hosted notebooks with free CPU/GPU/TPU resources | Resources are not guaranteed; runtime limits, accelerator availability and quotas fluctuate. Managed free runtimes prohibit remote-control/web-app use and long-running distributed workers. | [Official Colab FAQ and limits](https://research.google.com/colaboratory/intl/en-GB/faq.html) |

### Recently ended or not currently open

- **OpenAI 2026 Back-to-School Plus offer:** expired for new claims on **2026-10-31**; it was limited to eligible US college/graduate students. Do not present it as current. [Official terms](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students).
- **Anthropic Economic Futures awards:** the programme page states it is **not currently accepting applications**. It is a watch item, not a current offer. [Programme status](https://www.anthropic.com/economic-futures/program).
- **Modal academic programme:** local offer review reported new sign-ups closed on 2026-11-01. Because the current terms were not rechecked for this board, leave it out of current claimable offers until the official page is verified.

This board is a dated research aid, not a guarantee of entitlement or a global exhaustive list. Providers change eligibility, amounts and terms without notice. Recheck the primary source on the day of application and record new opportunities below as dated rows. Never publish a user's claim status, account identity, balance or application history here.

## Decision steps

1. Establish workload, required capabilities, users, privacy constraints and time horizon.
2. Check official provider pages and terms. Record exact date and eligibility; mark unverified claims as such.
3. Compare access route, total cost, caps, reliability, data handling, portability and lock-in against a no-change baseline.
4. Run a small task-specific evaluation before moving research or team work to a new model/access route.
5. Set usage limits and a stop date for trials; confirm who pays when credits expire or caps are reached.
6. Recheck before renewal, material model changes or external sharing. Update or expire stale rows rather than treating an old deal as current.

No application, purchase, subscription change or billing action follows from this tracker without the decision owner's explicit authorisation.

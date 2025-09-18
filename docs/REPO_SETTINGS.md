# Repository Settings Checklist

## 1) Branch protection for `main`
**Settings → Branches → New rule**  
Branch name pattern: `main`

Recommended checks:
- ☑ Require a pull request before merging
  - ☑ Require approvals: 1
  - ☑ Dismiss stale approvals when new commits are pushed
  - ☑ Require conversation resolution
- ☑ Require status checks to pass before merging
  - Select your CI workflow (e.g., `CI`)
  - ☐ Require branches to be up to date before merging (optional, safer)
- ☑ Require linear history
- ☐ Include administrators (optional)

## 2) Topics (About → ⚙ Edit)
Add topics to improve discoverability:
```
awareness, sdk, llm, offline, cli, prompts, mirroring, presence, resonance, conversational-ai, zh-tw
```

## 3) Description
Use a concise bilingual description:
- 面向覺察的對話 SDK：鏡映 / 臨在 / 頻率 / 共振四層管線，支援線上/離線 LLM、CLI 與可客製化 prompts。
- Awareness-focused dialog SDK: mirror, presence, frequency & resonance pipeline with online/offline LLM, CLI, and customizable prompts.

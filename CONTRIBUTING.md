# Contributing to Awareness SDK

感謝你願意為本專案貢獻！此文件說明從建立分支、提交變更到開 Pull Request（PR）的完整流程與規範。請在提出任何變更前，先閱讀以下內容。

---

## 快速開始（TL;DR）
```bat
# 取得最新 main
git checkout main
git fetch origin
git pull --rebase origin main

# 建立工作分支（請用有意義的名字）
git checkout -b docs/enhancement-001

# 開發、加入變更並提交
git add .
git commit -m "docs: refine contributing and PR template"

# 推到遠端並開 PR
git push -u origin docs/enhancement-001
# 之後到 GitHub：從 docs/enhancement-001 → main 建立 Pull Request

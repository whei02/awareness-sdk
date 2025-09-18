Param(
  [string]$CommitMessage = "Initial commit (min6, CLI & CI)"
)

Write-Host "Initializing git repo and pushing to https://github.com/whei02/awareness-sdk.git" -ForegroundColor Cyan
git init
git add .
git commit -m $CommitMessage
git branch -M main
git remote add origin "https://github.com/whei02/awareness-sdk.git"
git push -u origin main

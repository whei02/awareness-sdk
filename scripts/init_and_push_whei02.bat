@echo off
set REMOTE=https://github.com/whei02/awareness-sdk.git
set MSG=Initial commit (min6, CLI & CI)

echo Initializing git repo and pushing to %REMOTE%
git init
git add .
git commit -m "%MSG%"
git branch -M main
git remote add origin %REMOTE%
git push -u origin main

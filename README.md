> 面向覺察的對話 SDK：鏡映 / 臨在 / 頻率 / 共振四層管線，支援線上/離線 LLM、CLI 與可客製化 prompts。
>
> Awareness-focused dialog SDK: mirror, presence, frequency & resonance pipeline with online/offline LLM, CLI, and customizable prompts.

![CI](https://github.com/whei02/awareness-sdk/actions/workflows/ci.yml/badge.svg?branch=main)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)

<p align="center">
  <a href="https://github.com/YOUR_GH_USERNAME/awareness-sdk/actions/workflows/ci.yml">
    <img alt="CI" src="https://img.shields.io/github/actions/workflow/status/YOUR_GH_USERNAME/awareness-sdk/ci.yml?branch=main">
  </a>
  <a href="https://github.com/YOUR_GH_USERNAME/awareness-sdk/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-green.svg">
  </a>
  <a href="https://pypi.org/project/awareness-sdk/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/awareness-sdk.svg">
  </a>
  <a href="https://pepy.tech/project/awareness-sdk">
    <img alt="Downloads" src="https://img.shields.io/pypi/dm/awareness-sdk.svg">
  </a>
  <a href="https://github.com/YOUR_GH_USERNAME/awareness-sdk">
    <img alt="Stars" src="https://img.shields.io/github/stars/YOUR_GH_USERNAME/awareness-sdk?style=social">
  </a>
</p>


## Install (dev)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix/Mac: source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"
python -m pytest -q
```

## CLI
After install you can run:
```bash
awareness-cli --mode offline --input "hello"
```
or with Python:
```bash
python awareness_sdk/examples/quickstart_chat.py --mode auto
```


> Maintained by **Soul Insight Lab**

## Push to GitHub (Organization)
```bash
git init
git add .
git commit -m "Initial commit (org branded)"
git branch -M main
git remote add origin https://github.com/soul-insight-lab/awareness-sdk.git
git push -u origin main
```


## Quick Push (personal repo)
Push this repository to your GitHub account:

```bash
git init
git add .
git commit -m "Initial commit (min6, CLI & CI)"
git branch -M main
git remote add origin https://github.com/whei02/awareness-sdk.git
git push -u origin main
```

 [閱讀 Awareness-SDK 的願景文件](VISION.md)

import os
import sys
import argparse
import json
from pathlib import Path

from awareness_sdk.pipeline import AwarenessPipeline
from awareness_sdk.integrations.openai_client import OpenAIChat

def load_prompts(prompts_dir: Path) -> dict:
    cfg = {}
    try:
        import yaml  # type: ignore
    except Exception:
        yaml = None

    # frequency mapping
    fm = prompts_dir / "frequency_mapping.yaml"
    if fm.exists() and yaml:
        try:
            cfg["frequency_mapping"] = yaml.safe_load(fm.read_text(encoding="utf-8"))
        except Exception:
            pass
    # resonance templates
    rt = prompts_dir / "resonance_templates.yaml"
    if rt.exists() and yaml:
        try:
            cfg["resonance_templates"] = yaml.safe_load(rt.read_text(encoding="utf-8"))
        except Exception:
            pass
    # mirror template
    mt = prompts_dir / "mirror_layer.txt"
    if mt.exists():
        try:
            cfg["mirror_template"] = mt.read_text(encoding="utf-8")
        except Exception:
            pass
    return cfg

def build_pipeline(mode: str, prompts_cfg: dict | None) -> AwarenessPipeline:
    # Mode handling
    if mode == "offline":
        # Force fallback by ensuring no API key is visible
        os.environ.pop("OPENAI_API_KEY", None)
    elif mode == "online":
        if not os.getenv("OPENAI_API_KEY"):
            print("[ERROR] --mode online 但沒有設置 OPENAI_API_KEY。請先 setx OPENAI_API_KEY \"sk-...\" 後重開終端機。", file=sys.stderr)
            sys.exit(2)

    llm = OpenAIChat(model="gpt-4o-mini", temperature=0.3)
    config = {"disable_presence": False}
    if prompts_cfg:
        config["prompts"] = prompts_cfg
    return AwarenessPipeline(llm=llm, config=config)

def run_once(asp: AwarenessPipeline, text: str):
    resp = asp.respond(text, metadata={"locale": "zh-TW"})
    print("=== 覺察回應 ===")
    print(resp.text)
    print("\n=== META ===")
    try:
        print(json.dumps(resp.meta, ensure_ascii=False, indent=2))
    except Exception:
        print(resp.meta)

def run_repl(asp: AwarenessPipeline):
    print("Awareness SDK REPL（輸入空白行離開）")
    while True:
        try:
            text = input("> ").strip()
        except EOFError:
            break
        if not text:
            break
        run_once(asp, text)

def main():
    parser = argparse.ArgumentParser(description="Awareness quickstart with online/offline & custom prompts.")
    parser.add_argument("--mode", choices=["auto", "online", "offline"], default="auto",
                        help="推理模式：auto(預設)、online(需 OPENAI_API_KEY)、offline(強制走後備)")
    parser.add_argument("--prompts", type=str, default=None,
                        help="自訂 prompts 目錄（需包含 frequency_mapping.yaml / resonance_templates.yaml / mirror_layer.txt 任一）")
    parser.add_argument("--input", type=str, default=None,
                        help="單次輸入文字；省略則進入互動 REPL")
    args = parser.parse_args()

    prompts_cfg = None
    if args.prompts:
        pdir = Path(args.prompts)
        if not pdir.exists() or not pdir.is_dir():
            print(f"[WARN] 指定的 prompts 目錄不存在：{pdir}", file=sys.stderr)
        else:
            prompts_cfg = load_prompts(pdir)

    mode = args.mode
    if mode == "auto":
        mode = "online" if os.getenv("OPENAI_API_KEY") else "offline"

    asp = build_pipeline(mode, prompts_cfg)

    if args.input:
        run_once(asp, args.input)
    else:
        run_repl(asp)

if __name__ == "__main__":
    main()

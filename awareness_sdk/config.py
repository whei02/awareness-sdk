import json, os
DEFAULT = {"locale": "zh-TW", "presence": {"enabled": True}}

def load_config(path: str | None = None) -> dict:
    if not path or not os.path.exists(path):
        return DEFAULT
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data or DEFAULT
        except Exception:
            return DEFAULT

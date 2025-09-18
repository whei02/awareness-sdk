from .layers.mirror import mirror_reply
from .layers.frequency import detect_frequency
from .layers.resonance import value_resonance
from .layers.presence import presence_inject

class AwarenessPipeline:
    """
    ASP 主流程：Mirror → Frequency → Resonance → Presence
    """
    def __init__(self, llm, config: dict | None = None):
        self.llm = llm
        self.config = config or {}

    def respond(self, text: str, metadata: dict | None = None):
        meta = {"phases": {}, "labels": {}, "input": text}
        locale = (metadata or {}).get("locale", "zh-TW")

        # 1) Mirror
        m = mirror_reply(text, locale=locale)
        meta["phases"]["mirror"] = m

        # 2) Frequency
        freq = detect_frequency(text)
        meta["labels"]["frequency"] = freq

        # 3) Values/Resonance
        vals = value_resonance(text, freq)
        meta["labels"]["values"] = vals

        # 4) Compose prompt for LLM
        prompt = self._compose_prompt(text, m, freq, vals, locale)

        # 5) LLM Out
        raw_out = self.llm.generate(prompt)

        # 6) Presence inject
        final = presence_inject(raw_out, freq=freq, cfg=self.config)
        meta["phases"]["presence"] = {"applied": not self.config.get("disable_presence", False)}

        return type("Resp", (object,), {"text": final, "meta": meta})

    def _compose_prompt(self, text, mirror, freq, vals, locale):
        return f"""System: 你是覺察型對話導引者（語氣=接納/提問/留白；避免診斷與說教）。
Locale: {locale}
User: {text}
Mirror: {mirror}
Frequency: {freq}
Values: {vals}
Instruction:
- 先鏡映→再共鳴（以價值/需求為方向）→最後提供一個「當下覺察」的動作或提問。
- 只輸出 2~4 句，語氣溫和，不用條列清單。
"""

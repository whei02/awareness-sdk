import os

class OpenAIChat:
    """
    簡化的 LLM 介面：
    - 若環境有 OPENAI_API_KEY 且已安裝 openai 套件，則呼叫 OpenAI。
    - 否則走規則式後備生成（確保 demo 可離線運作）。
    """
    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.model = model
        self.temperature = temperature
        self._use_openai = False
        try:
            import openai  # noqa
            self._use_openai = bool(os.getenv("OPENAI_API_KEY"))
        except Exception:
            self._use_openai = False

    def generate(self, prompt: str) -> str:
        if self._use_openai:
            # 真實 API 呼叫
            from openai import OpenAI
            client = OpenAI()
            resp = client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            return resp.choices[0].message.content.strip()

        # 規則式後備（從 prompt 裡抓取提示線索做溫和回覆）
        lines = [ln.strip() for ln in prompt.splitlines() if ln.strip()]
        user = next((ln for ln in lines if ln.lower().startswith("user:")), "")
        mirror = next((ln for ln in lines if ln.lower().startswith("mirror:")), "")
        freq = next((ln for ln in lines if ln.lower().startswith("frequency:")), "")
        vals = next((ln for ln in lines if ln.lower().startswith("values:")), "")

        base = []
        if mirror:
            base.append(mirror.replace("Mirror:", "").strip())
        else:
            base.append("我在，先把你的感受放在這裡。")

        if "low" in freq or "140" in freq:
            base.append("這份感受是可以被理解的。")
        elif "high" in freq or "520" in freq:
            base.append("我感覺到你正處在很美好的能量狀態。")
        else:
            base.append("我們保持穩定，慢慢往前。")

        if "safety" in vals:
            base.append("你可能在尋找更多安全與支持。")
        elif "creativity" in vals:
            base.append("把這股靈感記下來，也許是下一步的起點。")

        return " ".join(base)

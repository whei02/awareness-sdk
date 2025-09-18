# 簡易詞典：可在 data/ 下用 YAML/JSON 擴充
LOW_WORDS = ["怕", "焦慮", "擔心", "不安", "羞愧", "愧疚", "憤怒", "沮喪", "難過"]
MID_WORDS = ["猶豫", "思考", "整理", "調整", "練習", "學習", "準備"]
HIGH_WORDS = ["喜悅", "感謝", "安心", "愛", "平和", "興奮", "充滿", "靈感", "自由"]

def detect_frequency(text: str):
    """
    以關鍵詞粗略偵測 Hawkins 風格頻率區段（僅示意）。
    回傳：
      score: 140/300/520（粗略代表低/中/高）
      band : "low" | "mid" | "high"
      cues : 命中的詞
    """
    cues = []
    score = 300

    if any(w in text for w in LOW_WORDS):
        score = 140
        cues = [w for w in LOW_WORDS if w in text]
    if any(w in text for w in HIGH_WORDS):
        score = 520
        cues = [w for w in HIGH_WORDS if w in text]
    if score == 300 and any(w in text for w in MID_WORDS):
        cues = [w for w in MID_WORDS if w in text]

    band = "low" if score < 200 else ("high" if score > 400 else "mid")
    return {"band": band, "score": score, "cues": cues}

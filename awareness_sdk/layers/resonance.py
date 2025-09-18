from collections import OrderedDict

# Schwartz / IDG 靈感的簡化價值維度（可配置）
VALUE_KEYWORDS = OrderedDict({
    "safety":  ["安全", "保障", "穩定", "養家", "風險"],
    "achievement": ["成就", "成果", "表現", "升遷", "突破"],
    "connection":  ["連結", "關係", "家人", "團隊", "朋友", "同伴"],
    "creativity":  ["創造", "靈感", "創新", "發想", "作品"],
    "meaning":     ["意義", "使命", "願景", "價值", "初心"],
})

def value_resonance(text: str, freq: dict):
    """
    以關鍵詞做最小價值映射，並依頻率微調權重。
    """
    weights = {k: 0.0 for k in VALUE_KEYWORDS.keys()}
    for k, kws in VALUE_KEYWORDS.items():
        hit = sum(1 for kw in kws if kw in text)
        weights[k] = float(hit)

    # 若沒有任何命中，依頻率給「合理先驗」
    if all(v == 0.0 for v in weights.values()):
        if freq["band"] == "low":
            weights["safety"] = 0.8
        elif freq["band"] == "high":
            weights["connection"] = 0.6
            weights["creativity"] = 0.4
        else:
            weights["meaning"] = 0.4

    # 正規化（避免全 0）
    s = sum(weights.values()) or 1.0
    for k in weights:
        weights[k] = round(weights[k] / s, 3)
    return weights

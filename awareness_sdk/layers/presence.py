def presence_inject(text: str, freq: dict, cfg: dict | None = None) -> str:
    """
    在尾端注入「當下引導」的一句話（可用 cfg 關閉）。
    """
    cfg = cfg or {}
    if cfg.get("disable_presence"):
        return text

    band = freq.get("band", "mid")
    if band == "low":
        tail = "先和我一起慢慢吸氣 4 拍、吐氣 6 拍，做 3 次。"
    elif band == "high":
        tail = "停留在這份能量裡，感受它在你胸口擴散 10 秒。"
    else:
        tail = "花 10 秒掃描身體感受，看看此刻最明顯的是什麼。"
    return f"{text}\n（當下引導）{tail}"

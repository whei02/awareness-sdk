---

# DEVELOPMENT.md

本文件記錄 **awareness-sdk** 的近期開發計畫與版本里程碑。
長期願景請參考 [`Roadmap.md`](./Roadmap.md)。

---

## 🎯 開發階段與里程碑

### v0.x (Foundations)

* [ ] 提供 **穩定的 CLI 工具 (`awareness-cli`)**，支援 `--mode` / `--prompts` 旗標
* [ ] 實作 **離線 fallback 模式**，並完成文件與測試
* [ ] 發布 **最小範例 (Minimal examples)** 與 **教學 notebook**
* [ ] 撰寫 **基本 prompts 自訂指南**

---

### v0.1

* [ ] **Pluggable LLM 接口**（可替換模型）與設定檔範例
* [ ] 延伸 prompts：支援 **frequency / resonance** 與 **多語系在地化**
* [ ] 新增 **Logging / Telemetry hooks**

---

### v0.2

* [ ] 發布 **PyPI 套件**，支援 `pip install awareness-sdk`
* [ ] 增加單元測試覆蓋率，並在 CI 中掛上 **Coverage badge**
* [ ] 提供 **應用整合範例**（與 AI/CV pipeline, API server 等）

---

### v1.0 (Stability)

* [ ] **穩定公開 API** (Stable public APIs)
* [ ] 宣告 **Backward compatibility 承諾**
* [ ] 架設 **官方文件網站 (Docs site)**

---

## 📌 管理方式

* 使用 **GitHub Projects / Milestones** 追蹤進度
* 每個版本 milestone 建立對應的 issue / PR
* 定期更新此文件，確保與實際開發同步

---

要不要我順便幫你產生一個 **GitHub Project / Milestone 配置範例**（像是 v0.1 backlog issue 清單）？這樣你可以直接丟進 issue tracker 用。

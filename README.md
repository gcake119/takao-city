# Takao City Coordination

本 repository 是鹽埕區公所出納工作台的 coordination repo，用來保存跨前後端共同依據，不承載可執行的產品程式碼。

## 收錄內容

- 需求與產品範圍。
- POC／Trial 規劃。
- 架構決策與資料契約基線。
- 前後端工作拆解與協調紀錄。
- 跨 repo 驗收情境與結果。

## Repository 分工

- Coordination：本 repository。
- Frontend：[`gcake119/takao-city-frontend`](https://github.com/gcake119/takao-city-frontend)，負責 Vue 3 應用程式。
- Backend：[`gcake119/takao-city-backend`](https://github.com/gcake119/takao-city-backend)，負責 NestJS API、Drizzle ORM 與 SQLite。
- Document Engine：[`gcake119/takao-document-engine`](https://github.com/gcake119/takao-document-engine)，負責以 Python 從紙本文件電子檔擷取候選欄位。

前後端以 OpenAPI 作為協作契約。後端負責產生 OpenAPI，前端使用 Orval 產生 TypeScript API Client，不在 coordination repo 放置前後端執行程式碼。

文件引擎不直接寫入工作台資料庫。擷取結果必須由後端驗證並經承辦人確認後才能保存；文件引擎是否納入第一階段 Trial，另行決定。

## 目前規劃

- [鹽埕區公所秘書室出納工作台 POC 規劃](docs/plans/2026-09-19-鹽埕區公所出納工作台-POC-規劃.md)
- [已被取代的採購工作台規劃](docs/plans/2026-09-19-鹽埕區公所採購工作台-POC-規劃.md)

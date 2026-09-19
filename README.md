# Takao City Coordination

本 repository 是鹽埕區公所採購工作台的 coordination repo，用來保存跨前後端共同依據，不承載可執行的產品程式碼。

## 收錄內容

- 需求與產品範圍。
- POC／Trial 規劃。
- 架構決策與資料契約基線。
- 前後端工作拆解與協調紀錄。
- 跨 repo 驗收情境與結果。

## Repository 分工

- Coordination：本 repository。
- Frontend：Vue 3 應用程式，使用獨立 repository；名稱與連結待建立。
- Backend：NestJS API、Drizzle ORM 與 SQLite，使用獨立 repository；名稱與連結待建立。

前後端以 OpenAPI 作為協作契約。後端負責產生 OpenAPI，前端使用 Orval 產生 TypeScript API Client，不在 coordination repo 放置前後端執行程式碼。

## 目前規劃

- [鹽埕區公所秘書室採購工作台 POC 規劃](docs/plans/2026-09-19-鹽埕區公所採購工作台-POC-規劃.md)

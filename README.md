
# CJC101-FastAPI

這是一個使用 FastAPI 建立的簡單 REST API 範例，功能包含：

- 新增使用者資料（POST /user/add）
- 查詢所有使用者資料（GET /users）
- 依 ID 查詢單一使用者資料（GET /user/{user_id}）
- 更新使用者資料（PUT /user/{user_id}）
- 刪除使用者資料（DELETE /user/{user_id}）
- 根路由簡單歡迎訊息（GET /）

## 專案架構

```
fastapi_app/
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── user_data/        # 使用者資料存放目錄（容器內）
└── README.md
```

- `main.py`：FastAPI 程式主檔
- `Dockerfile`：建立 Python 環境及啟動 FastAPI
- `docker-compose.yml`：Docker Compose 設定
- `requirements.txt`：Python 相依套件
- `user_data/`：用來儲存使用者 JSON 資料的資料夾（執行時自動建立）

---

## 快速開始

### 1. 使用 Docker Compose 建置並啟動

```bash
docker-compose up --build
```

### 2. 開啟瀏覽器，查看 Swagger API 文件

```
http://localhost:8000/docs
```

---

## API 介面

1. API 服務預設監聽在 http://localhost:8000

2. 你可以用 curl 或 Postman 測試 API：

- 根路由：

```bash
curl http://localhost:8000/
```

- 新增使用者：

```bash
curl -X POST http://localhost:8000/user/add -H "Content-Type: application/json" -d '{"id":"1","name":"Alice","email":"alice@example.com"}'
```

- 查詢所有使用者：

```bash
curl http://localhost:8000/users
```

- 依 ID 查詢使用者：

```bash
curl http://localhost:8000/user/1
```

- 更新使用者：

```bash
curl -X PUT http://localhost:8000/user/1 -H "Content-Type: application/json" -d '{"id":"1","name":"Alice Updated","email":"alice_new@example.com"}'
```

- 刪除使用者：

```bash
curl -X DELETE http://localhost:8000/user/1
```

## 注意事項

- 使用者資料會以 JSON 檔案存放在 `user_data/` 資料夾中
- 請確保容器有權限讀寫該資料夾
- Docker 掛載 volume 時，確認資料夾同步正常
- 若需修改監聽埠號，可調整 `docker-compose.yml` 及 `Dockerfile`
- 如果要新增或修改 API，請修改 `main.py`

---

## 授權

MIT License © 2025 [whfan96](https://github.com/whfan96)


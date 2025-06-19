# cjc101-fastapi

一個基於 FastAPI 的簡易使用者資料管理 API，支援新增、查詢所有及查詢單一使用者功能。  
專案已 Docker 化並可透過 docker-compose 快速啟動。

---

## 專案結構

```
fastapi_app/
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── user_data/        # 使用者資料存放目錄（容器內）
└── README.md
```

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

### 新增使用者

- 路徑：`POST /user/add`
- 範例請求資料：

```json
{
  "id": "001",
  "name": "Alice",
  "email": "alice@example.com"
}
```

### 取得所有使用者

- 路徑：`GET /users`

### 取得指定使用者

- 路徑：`GET /user/{user_id}`

---

## 本機開發測試

1. 安裝依賴套件：

```bash
pip install -r requirements.txt
```

2. 啟動 FastAPI 服務：

```bash
uvicorn main:app --reload
```

---

## 注意事項

- 使用者資料會儲存在 `user_data` 資料夾的 JSON 檔案中，請確保該資料夾存在且有寫入權限。
- Docker 掛載 volume 時，確認資料夾同步正常。
- 如果要新增或修改 API，請修改 `main.py`。

---

## 授權

MIT License © 2025 [whfan96](https://github.com/whfan96)



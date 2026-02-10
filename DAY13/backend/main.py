from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定（JSから呼ぶために必須）
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/hello")
def hello(name: str):# クエリのnameから値を取得し変数nemeに自動で代入している
    return {"message": f"こんにちは、{name}さん！"}
  
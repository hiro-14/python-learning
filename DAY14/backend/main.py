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

@app.get("/api/hello")
def say_hello(name: str):# クエリのnameから値を取得し変数nemeに自動で代入している
    """
    <docstring>
    名前を受け取り、挨拶文を返すAPI
    """
    return {"message": f"こんにちは、{name}さん！"}
  
from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# 起動時にモデルをダウンロード
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def root():
    return {"message": "AI API is running"}

@app.get("/predict")
def predict(x1: float, x2: float):
    data = np.array([[x1, x2]])
    prediction = model.predict(data)

    return {
        "input": [x1, x2],
        "prediction": int(prediction[0])
    }
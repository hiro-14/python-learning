import pickle

# モデル読み込み
with open("model.pkl", "rb") as f:
  loaded_model = pickel.load(f)

print("モデル読み込み完了")

import numpy as np
sample = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = loaded_model.predict(sample)

print("予測結果：", prediction)



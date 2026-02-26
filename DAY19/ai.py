from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import pickle

# データ読み込み
data = load_iris()
X = data.data
y = data.target

# 分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# モデル作成
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# モデルを保存する
with open("model.pkl", "wb") as f:
  pickle.dump(model, f)
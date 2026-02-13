from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# データ読み込み
iris = load_iris()
X = iris.data
y = iris.target

# 学習用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7,)

    # データを80%学習用、20%テスト用に分割


# モデル作成
model = DecisionTreeClassifier()

# データからパターンを学習
model.fit(X_train, y_train)

# 予測
y_pred = model.predict(X_test)
  # X = 入力(特徴量)、y = 出力(正解ラベル)

# 精度評価（正解数/全体数）
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
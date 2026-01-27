import pandas as pd
import matplotlib.pyplot as plt

#　csv読み込み
df = pd.read_csv(r"C:\Users\life\python-learning\DAY5\scores.csv")

# グラフ作成
# 生徒ごとの点数を比較しやすくするため、棒グラフを使用
plt.bar(df["name"], df["score"])
plt.xlabel("Name")
plt.ylabel("Score")
plt.title("Test Scores")

plt.show()
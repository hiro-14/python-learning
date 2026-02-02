import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv(r"/Users/GitHub/python-learning/DAY5/scores.csv")

# fig = グラフ全体（1ページのキャンバス）
# ax = 描画領域（実際に描く１つのグラフ領域）
fig, ax = plt.subplots() # 1行1列のグラフ領域を作成
# fig, ax = plt.subplots(2, 2)の場合、2行2列のグラフ領域を作成

# データの並べ替え
df_sorted = df.sort_values("score", ascending=False)

ax.bar(df_sorted["name"], df_sorted["score"], color="skyblue")
ax.set_xlabel("Name")
ax.set_ylabel("Score")
ax.set_title("Test Scores")
ax.set_ylim(0, 100) # y軸の範囲設定

for i, v in enumerate(df_sorted["score"]): # enumerateで番号と値を同時に取り出す、番号を自動で付けてくれる for 文
  ax.text(i, v+1, str(v), ha="center") # 棒グラフの上に数値を表示

plt.show()

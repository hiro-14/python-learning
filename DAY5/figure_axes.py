import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv(r"/Users/GitHub/python-learning/DAY5/scores.csv")

fig, ax = plt.subplots()

# データの並べ替え
df_sorted = df.sort_values("score", ascending=False)

ax.bar(df_sorted["name"], df_sorted["score"], color="skyblue")
ax.set_xlabel("Name")
ax.set_ylabel("Score")
ax.set_title("Test Scores")
ax.set_ylim(0, 100)

for i, v in enumerate(df_sorted["score"]):
  ax.text(i, v+1, str(v), ha="center")

plt.show()

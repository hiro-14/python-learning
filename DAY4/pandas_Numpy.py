# CSVとは...カンマ区切りのテキスト
 # Excelで開ける
 # ただのテキスト
 # プログラムから扱いやすい形式(特にpandas)

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "scores.csv"

df = pd.read_csv(csv_path)
print(df)

average = df["score"].mean()
print("平均点：", average)

max_score = df["score"].max()
print("最高点：", max_score)

result_df = pd.DataFrame({
  "average_score": [average],
  "max_score": [max_score]
})

result_df.to_csv("result.csv", index=False)
# if文 条件によって処理を分ける
score = 75
if score >= 60:
    print ("合格")
else:
    print ("不合格")

# if文　演習
age = 23
if age >= 20:
    print ("成人です")
else:
    print ("未成年です")

# for文　複数のデータを1つずつ処理する
scores = [80, 65, 90]

for s in scores:
    print (s)

# for文　演習
names = ["Alice","Bob", "Charlie" ]

for name in names:
    print (name)

# list 順番を持った複数データ
scores = [80, 65, 90]
print(scores[0]) # listは0からスタート

# list 演習
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# dict キーと値のセットでデータ管理
student = {
    "name": "Taro",
    "score": 75        # キー: 値
}

print (student["name"])

# for × dict
students = {
    "A": 80,
    "B": 55,
    "C": 90
}

for name, score in students.items():
    print (name, score)

# DAY2 メイン課題　点数から合否を判定

 # 私の回答
scores = {
    "A": 55,
    "B": 80,
    "C": 90
}

for name, score in scores.items():

    if score >= 60:
        print (name, "合格")
    else:
        print (name, "不合格")

 # 模範解答
scores = {
    "Aさん": 80,
    "Bさん": 55,
    
    "Cさん": 70
}

for name, score in scores.items():
    if score >= 60:
        result = "合格" # 判定結果を変数に
    else:
        result = "不合格"

    print(name, score, result)


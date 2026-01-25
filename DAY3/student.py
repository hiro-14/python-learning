class Student:
  def __init__(self, name, score):
    self.name = name
    self.score = score
  
  def judge(self):
    return "合格" if self.score >= 60 else "不合格"
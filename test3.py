import random

class xList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

x_list = xList(["A", "B", "C", "D", "E"])
print(len(x_list))
print(len(x_list))
print(x_list[2])
print (x_list[2])



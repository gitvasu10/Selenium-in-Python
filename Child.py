from Demo1 import Calculator
class Child(Calculator):
    num2 = 201

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj2 = Child()
print(obj2.getCompleteData())

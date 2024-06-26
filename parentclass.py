class Calculator:
    num = 100
    def __init__(self, a, b):
        self.f_num = a
        self.l_num = b

    def summation(self):
        return self.f_num + self.l_num + self.num

obj = Calculator(4, 10)
print(obj.summation())
print(obj.num)
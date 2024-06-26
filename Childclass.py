from parentclass import Calculator

class Childclass(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 6, 10)

    def check_value(self):
        return self.num2 + self.num + self.summation()


obj =  Childclass()
print(obj.check_value())
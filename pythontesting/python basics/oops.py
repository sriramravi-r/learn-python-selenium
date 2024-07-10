# class
class Calculator:
    num=1

    def __init__(self,a,b):
        print("i am called automatically")
        self.A=a
        self.B=b
    def getData(self):
        print("I am now executing as method in class")

    def add(self):
        return self.A + self.B + Calculator.num

print("out side of class")
objCalculator=Calculator(2,3) #syntax to create a object in python
objCalculator.getData();
print(objCalculator.num)
print(type(objCalculator))
print(objCalculator.add())
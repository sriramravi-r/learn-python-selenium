from oops import Calculator

class childimplement(Calculator):
    num2=2

    def __init__(self):
        Calculator.__init__(self,2,3)
    def getCompleteData(self):
        print("================================")
        return childimplement.num2 + Calculator.num + Calculator.add(self)

objchildimplement=childimplement()
print(objchildimplement.getCompleteData())

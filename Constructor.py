#self keyword is mandotary for calling variable names into method
#instance and class variables have whole different purpose
#Constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100 #class variable
    #default constructor

    def __init__(self,a,b):
        self.firstname= a
        self.secondname= b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstname + self.secondname + self.num

obj = Calculator(2,3) #syntax to create obj in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5) #syntax to create obj in python
obj1.getData()
print(obj1.Summation())
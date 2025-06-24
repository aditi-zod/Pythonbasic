#Classes are user defined blueprint or prototype
# Sum, Multiplication, substractions, constant
# methods, Class variable, instance variable, constructor etc

class Calculator:
    num = 150

    def getData(self):
        print("I am now executing as method in class")

obj = Calculator() #syntax to create obj in python
obj.getData()
print(obj.num)
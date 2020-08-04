class ClassA:
    a,b=10,20
    def display():
        print("i am form classA")

class ClassB(ClassA):
    c,d=23,78
    def show():
        print("i am from classB")

obj=ClassB
print(obj.d)
obj.display()

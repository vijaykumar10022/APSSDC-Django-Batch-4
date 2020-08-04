class A:
    def classA():
        print("im from class A")

class B:
    def classB():
        print("im from class B")

class C(A,B):
    def classC():
        print("im from classC")


obj=C
obj.classA()
obj.classC()
obj.classB()

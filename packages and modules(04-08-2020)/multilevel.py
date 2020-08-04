class A:
    def classA():
        print("im from class A")

class B(A):
    def classB():
        print("im from class B")

class C(B):
    def classC():
        print("im from classC")


obj=C
obj.classA()
obj.classC()
obj.classB()

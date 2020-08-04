class Math:
    def __init__(abc,v1,v2):
        abc.v1=v1
        abc.v2=v2
    def show(abc):
        print(abc.v1)
        print(abc.v2)
    def add(abc):
        return abc.v1+abc.v2

m=Math(4,5)
print(m.show())
print(m.add())

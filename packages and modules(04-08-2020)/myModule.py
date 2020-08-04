class Calsi:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2

class Math:
    def power(bval,exval):
        return bval**exval
    def isEven(val):
        if val%2==0:
            return True
        return False


def isOdd(val):
    if val%2!=0:
        return True
    return False


class Calsi1:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def __add__(self):
        return self.v1+self.v2
    def __mul__(self):
        return self.v1*self.v2
    

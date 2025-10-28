"""a='4'
b='6'
print(a+b)
print(str.__add__(a,b))"""

'''
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3 =student(m1,m2)
        return s3

s1 = student(58,69)
s2 = student(60,65)

s3 = s1+s2

print(s3.m1)'''


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other): #overloading by using add method
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3 =student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1 +self.m1
        r2=self.m2 +self.m2
        if r1>r2:
            return True
        else:
            return False

s1 = student(58,69)#object
s2 = student(60,65)#object, so we cant do add directly

s3 = s1+s2

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")


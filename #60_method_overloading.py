#method overloading= a class which is having same name with diff arguments/parameters is called method overloading
#method overriding= a class which is having same name and same parameters is called method overriding

'''class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a,b,c):
        s=a+b+c
        return s
s1=student(55,69)
print(s1.sum(5,9,6))'''

'''class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=student(55,69)
print(s1.sum(5,6,7))'''

class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")


a1=B()
a1.show()

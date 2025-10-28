#inheritance- it means it inherit the properties and methods from another class

#single level inheritance
'''class A: 
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
a1=A()
a1.feature1()
a1.feature2()'''

#multi-level inheritance
'''
class A: #grandparent class
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
#parent class    
class B(A): #here b inheriting the features of AA
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")
class C(B):#child class
    def feature5(self):
        print("feature 5 working")
a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

'''
#multiple inheritance

class A: #parent class
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
#parent class    
class B: #here b inheriting the features of AA
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")
class C(A,B):#child class
    def feature5(self):
        print("feature 5 working")
a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

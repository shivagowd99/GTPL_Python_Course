'''class A: 
    def __init__(self): #constructer
        print("in A Init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A): 
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

a1=B()''' #it consider class A constructer and print because we have no constructer in sub class


'''class A: #superclass
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A): #subclass
    def __init__(self):
        print("in B Init")
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

a1=B() #it consider sub class i mean class b because if we have constructer in both super class and sub class it consider only sub class constructer
'''

'''class A: #superclass
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A): #subclass
    def __init__(self):
        super().__init__() #here im using super class features
        print("in B Init")
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

a1=B()
'''

class A: 
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("feature 1-A working")
    def feature2(self):
        print("feature 2 working")

class B: 
    def __init__(self):
        super().__init__() #here im using super class features
        print("in B Init")
    def feature3(self):
        print("feature 1-B working")
    def feature4(self):
        print("feature 4 working")

class c(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")

c1=c()

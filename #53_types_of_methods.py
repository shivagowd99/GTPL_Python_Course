#types of methods - instance methods , class methods, static methods

#constructer - it is used for alloacting some data like variables and methods
'''
class student:
    school ="geetam"
    def __init__(self,m1,m2,m3): 
        self.m1=m1 
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3 #calculating average

s1 = student(23,45,78)
s2 = student(66,45,67)

print(s1.avg())
print(s2.avg())'''


'''class student:
    school ="geetam"
    def __init__(self,m1,m2,m3): 
        self.m1=m1 
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3 #calculating average
    @classmethod
    def info(cls):
        return cls.school

s1 = student(23,45,78)
s2 = student(66,45,67)

print(s1.avg())
print(student.info())'''


class student:
    school ="geetam"
    def __init__(self,m1,m2,m3): 
        self.m1=m1 
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3 #calculating average
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod #it is used for giving general information

    def info():
        print("This is student.. in abc module")

s1 = student(23,45,78)
s2 = student(66,45,67)

print(s1.avg())
print(student.getschool())

student.info()
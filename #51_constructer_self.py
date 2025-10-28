#while using objects it takes some space in heap memory
 
'''class computer:
    pass
c1= computer()
print(id(c1))'''

 
'''class computer:
    def __init__(self):
        self.name ='shiva'
        self.age =25
c1= computer()
c2= computer()
c1.name ='nezuko'
c1.age =12
print(c1.name)
print(c2.name)'''


class computer:
    def __init__(self):
        self.name ='shiva'
        self.age =25
    def update(self):
        self.age = 30
    def compare(self,other):
       if self.age==other.age:
          return True
       else:
          return False

c1= computer()
c1.age =30
c2= computer()
if c1.compare(c2): #compare(who is calling,whom to compare)
   print("they are same")
else:
   print("They are different")

print(c1.name)
print(c2.name)

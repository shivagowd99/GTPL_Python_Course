#the variables which are defined inside init method those are called instance variables 
#the variables which are defined inside class and outside of init method is called class or static variables
'''class car:
    def __init__(self):
        self.mil = 10    #instance variables
        self.com = 'BMW'  #instance variables
    
c1=car()
c2=car()
print(c1.com,c2.mil)
print(c2.com,c1.mil)'''


class car:
    wheels =4  #class variables/static variable
    def __init__(self):
        self.mil = 10    #instance variables
        self.com = 'BMW'  #instance variables
    
c1=car()
c2=car()
print(c1.com,c2.mil,c1.wheels)
print(c2.com,c1.mil,c2.wheels)


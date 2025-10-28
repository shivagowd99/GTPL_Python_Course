#init method - it is used for initialising variables and methods

class computer: #created class with class name as computer
    def __init__(self,cpu,ram): #init is used for to intialising variables and methods
        self.cpu =cpu
        self.ram =ram
        
    def config(self): 
        print("config is",self.cpu,self.ram)

com1 = computer('i5',16) #com1 is obj and computer is constructer
com2 = computer('Ryzen 3',8)

com1.config() #here directly calling objname.methodname this is another way to access
com2.config()



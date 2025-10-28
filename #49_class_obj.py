#class = class is nothing but a design?blueprint of object

#object - obj is a instance of class and it is having attributes and behaviour

'''class computer: #created class with class name as computer
    def config(self): #self is nothing but a object we are passing
        print("i5,16gb,1TB")

x=9    
print(type(x))
a='8'
print(type(a)) #type of a is string
com1 = computer() #object
print(type(com1)) #comp1 is an object of computer
                  #it gives o/p like '__main__.computer'

'''


class computer: #created class with class name as computer
    def config(self): 
        print("i5,16gb,1TB")

com1 = computer() #object
com2 = computer()
computer.config(com1) #for accesing methods we have to call like classname.methodname
computer.config(com2)
com1.config() #here directly calling objname.methodname this is another way to access
com2.config()
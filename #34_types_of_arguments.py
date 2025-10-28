'''def add(a,b):  #here a,b we call formal arguments
    c=a+b
    print(c)
add(5,6) #its actual arguments(actually we have 4 types - position,keyword,default,variable length)
'''
'''#program for position arguments
def person(name,age):
    print(name)
    print(age)
person('shiva',25)'''

'''#program for keyword arguments
def person(name,age):
    print(name)
    print(age)
person(age=25,name='shiva')'''

'''#program for default arguments
def person(name,age=20):  #its default value ,if we not given actual value then this default value prints
    print(name)
    print(age)
person(name='shiva',age=25)'''


#program for variable length arguments
'''def sum(a,*b):
    c=a+b
    print(c)
sum(5,6,23,45)''' #its program get error because int and tuple are unsupported operands

def sum(a,*b): #here a stores 5 and remaining all values stores in b
    c=a 
    for i in b: #it takes one one value from tuple and add
        c=c+i
    print(c)
sum(5,3,23,54)

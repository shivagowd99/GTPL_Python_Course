#function- block of code that performs specific tasks
'''def shiva(): #defining function and function name
    print("hello")
    print("good morning")
    
shiva()
'''

'''def add(x,y): #definining func and func name of variables x and y
    c=x+y
    return c #it sends a value back where it called and it is stores and we can reuses 
result=add(5,6)
print(result) #it shows information on display if we use
'''
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,6)
print(result1,result2)


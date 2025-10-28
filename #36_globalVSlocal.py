'''a=10
def num():
    a=5 #first preference is local variable
    print(a)
num()
print("outside",a)'''

#we can use global variable inside and outside funtion too
'''a=10
def num():
    print(a)
num()
print("outside",a)'''

#program to use local variable as global variable
a=10
def num():
    global a
    a=5 
    print(a)
num()
print("outside",a)
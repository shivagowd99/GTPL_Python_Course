def update(x):
    print(id(x)) #it gives actual id value
    x=8
    print(id(x))  #it gives new id
    print("x ",x)
a=10
print(id(a))
update(a)
print("a ",a)
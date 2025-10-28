"""def person(name,**data): #for sending multiple data we have to use ** for keyword variable length arguments
    print(name)
    print(data)
person('shiva',age=25,city='amalapuram',mob=9121899534)"""


def person(name,**data): #for sending multiple data we have to use ** for keyword variable length arguments
    print(name)
    for i,j in data.items(): 
        print(i,j)
person('shiva',age=25,city='amalapuram',mob=9121899534)


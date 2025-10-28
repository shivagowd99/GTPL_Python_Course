'''x=int(input("how many hours u play bgmi?"))
i=1
while i<=x:
    print("bgmi")
    i=i+1

'''
'''
#program using break statement
for i in range(10):
    if i==5:
        break
    else:
        print(i)
'''
'''
#program using continue statement
for i in range(10):
    if i==5:
        continue
    else:
        print(i)'''
'''
for i in range(1,101): #i have taken 1 to 1oo numbers range
    if i%3==0 and i%5==0: #i want which are not divisible by 3 and 5 those values continue
        continue
    print(i)'''
#program for pass statement
for i in range(1,101):
    if i%2!=0:
        pass
    print(i)
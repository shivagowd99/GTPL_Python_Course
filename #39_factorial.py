#factorial
n= int(input("enter a number")) #reading data from console
fact=1 
for i in range(1,n+1): #incrementing values
    fact=fact*i 
print(fact)

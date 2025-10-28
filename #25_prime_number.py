#prime number -its is nothing but a its divisible by 1 and itself

#program to check it is prime number or not
n=10
for i in range(2,n):
    if n%i==0:
       print("Not prime")
       break
else:
   print("prime") 
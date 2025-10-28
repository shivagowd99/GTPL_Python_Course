#we have import math function for doing mathematical calculations
import math
x=math.factorial(5)
print(x) #for factorial value we use factorial functiom


x=math.sqrt(5)
print(x)  #for square root functions we use sqrt function

x=math.floor(2.5)
print(x) #if we use floor function it floor down the value

x=math.ceil(2.5)
print(x) #if we use ceil function it ceils up the value

x=math.pow(3,2)
print(x) #power function is nothing eponential function

print(math.pi)

print(math.e)


#we can import specific functions like this ,here no need to specify math fuction every time

from math import pow,factorial
x=factorial(5)
print(x)

x=pow(3,2)
print(x)
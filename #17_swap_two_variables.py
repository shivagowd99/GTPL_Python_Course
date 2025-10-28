#swapping two numbers by using third variable
a=5
b=6
temp=a
a=b
b=temp
print(a)
print(b)

#swapping two numbers without using third variable
a=5
b=6
a=a+b #5+6=11
b=a-b #11-6=5
a=a-b #11-5=6
print(a)
print(b)

a=5
b=6
a,b=b,a
print(a)
print(b) 
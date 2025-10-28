'''#program to print 10 fibanocci numbers
def fib(n):
    a=0 
    b=1
    print(a) #printing because im incrementing from second number in for loop
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(1)'''

#program to print  fonly 1 fibanocci number
def fib(n):
    a=0 
    b=1
    if n==1:
        print(a)
    else:
        print(a) #printing because im incrementing from second number in for loop
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(5)


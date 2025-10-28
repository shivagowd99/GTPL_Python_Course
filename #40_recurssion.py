#recursion - a fun call by itself 
def fact(n):
    if n==0 or n==1: #i have given condition like if my number is equal to 0 or 1 then return 1
        return 1 
    else:
        return n*fact(n-1)
    
print(fact(5))
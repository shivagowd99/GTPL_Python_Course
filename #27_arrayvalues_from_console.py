from array import *
arr=array('i',[]) #created empty array
n=int(input("enter the length of array")) #reading data from console
for i in range(n): 
    x=int(input("Enter the next value"))
    arr.append(x)
print(arr)

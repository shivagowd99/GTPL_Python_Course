#numpy - it is one of library in python , it is used for doing numerical operations and it supports multidimensional arrays and matrices

from numpy import *
'''arr=array([1,2,5,3,7]) #In numpy no need to specify datatype
print(arr)
'''
'''arr=array([1,2.5,5,3,7]) #if we give float values with integers its convert like float values
print(arr)'''

'''arr=array([1,2,5,3,7],float)
print(arr)'''

#linspace also works like range function start,stop,step
'''arr=linspace(0,15,16) #here step value divides so we get value in float
print(arr)'''

'''arr=logspace(1,40,5) #here o/p gives like float with combination e values
print(arr)'''

'''arr=zeros(5)
print(arr)'''

arr=ones(5)
print(arr)
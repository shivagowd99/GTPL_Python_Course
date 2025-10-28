#matrix - it is nothing but a data there in combination of rows and cols
from numpy import *
#program to print two dimensional array
'''arr  = array([
             [1,2,3], #ndim is for dimensions
             [4,5,6]    #size method to get how many values in matrix
])
print(arr)'''


#program to cconvert two dimensional to one dimensional
'''arr  = array([
             [1,2,3,6,2,9], 
             [4,5,6,7,5,3]    
            ])
arr2=arr.flatten() #flatten means it print in i
print(arr2)
'''

#program to convert two dimensional to three dimensional
'''arr  = array([
             [1,2,3,6,2,9], 
             [4,5,6,7,5,3]    
            ])
arr2=arr.reshape(3,4)
print(arr2)'''

'''m=matrix('1 2 3;4 5 6;7 8 9')
print(m)''' #it print 3rows and 3 coloumns

'''m=matrix('1 2 3;4 5 6;7 8 9')
print(diagonal(m))    #diagonal = cross
print(m.max())
print(m.min())'''


m1=matrix('1 2 3;4 5 6;7 8 9')
m2=matrix('1 2 3;4 5 6;7 8 9')
m3=m1+m2
print(m3)



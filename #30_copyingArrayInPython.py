from numpy import *
'''arr=array([1,2,3,4,5])
arr = arr+5 #adding 5 to every element
print(arr)'''

'''arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])
arr3=arr1+arr2 #it combines both vales
print(arr3)
'''
'''arr=([1,2,3,4,5])
#print(sqrt(arr))
#print(sum(arr))
print(log(arr))
'''
'''
arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])
print(concatenate([arr1,arr2])) #we can concatenate by using this function
'''

'''arr1 =array([1,2,3,4,5])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))'''

arr1=array([1,2,3,4,5])
arr2=arr1.view() #view, it helps to create new array in new id location
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
#program to check list of even numbers using lambda functions
#def is_num(n):
#    return n%2==0
'''
nums=[2,4,5,3,6,8,7,9,6,4]
evens=list(filter(lambda n : n%2==0,nums)) #here i used filter function for filtereing even numbers
print(evens)'''


'''nums=[2,4,5,3,6,8,7,9,6,4]
evens=list(filter(lambda n : n%2==0,nums)) #here i used filter function for filtereing even numbers
doubles=list(map(lambda n : n*2,evens)) #here double the evens
print(doubles)'''

from functools import reduce
nums=[2,4,5,3,6,8,7,9,6,4]
evens=list(filter(lambda n : n%2==0,nums)) #here i used filter function for filtereing even numbers
doubles=list(map(lambda n : n*2,evens)) #here double the evens
sum=reduce(lambda a,b:a+b,doubles) #here reduce used for getting single value i mean sum
print(sum)



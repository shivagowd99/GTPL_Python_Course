#program to print even and odd values from list using functions
def count(lst):
    even=0
    odd=0
    for i in lst: #for increment the values used for loop
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[22,33,54,67,87,46,89]
even,odd =count(lst)
print(even)
print(odd)
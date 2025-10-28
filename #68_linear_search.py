#Linear search - It means checking each element of the list one by one from start to end until we find the number we want.
pos= -1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
list=[5,6,3,7,8,9,3]
n=5
if search(list,n):
    print("found at",pos+1)
else:
    print("Not found")
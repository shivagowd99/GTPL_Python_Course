#arrays- arrays are used to store multiple values ,if we declare an array the size will be fixed . we cant change array size because its in fixed size

from array import * 
'''vals = array('i',[22,33,44,76]) #i is nothing but a integer because we are stored all integer values 
print(vals)
'''
'''
vals = array('i',[5,9,-8,4,2])
for i in range(5):
    print(vals[i])
'''
#program to mutiply values using array concept
vals =array('i',[2,5,4,7,6,8]) 
newArray = array(vals.typecode, (a*a for a in vals)) #when we dont know what type the value is then take typecode method
i=0                                                #(a*a for a in vals)means i dont know vals ans take one one vals from array and multiple
for e in newArray:
    print(e,end=" ")
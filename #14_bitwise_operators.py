#bitwise-it works directly on the binary (bit-level) representation of integers
#we have and ,or xor,left shift and right shift, compliment operators
#program for compliment operator 
x= ~12 #-(a+1)
print(x) #00001100 =12
         #1's compliment of 00001100 is 11110011 and do 2's compliment to this By adding +1 = 00001101 by inverting all bits we get this number

#program for and operator
#In And operator both should be true 
a=12         #12-00001100
b=13         #13-00001101
c=a&b        #0/p-00001100 =12
print(c) 


#program for Or operator
#In Or operator atleast one should be true then true
a=12         #12-00001100
b=13         #13-00001101
c=a|b        #0/p-00001101 =13
print(c)



#program for Xor operator
#In Xor operator atleast one should be true then true
a=12         #12-00001100
b=13         #13-00001101
c=a^b        #0/p-00000001=1
print(c)

#program to left shift operator
a=10    #00001010
b=a<<2  #00101000 =32+8=40
print(b) 

#program to Right shift operator
a=10   #10100000
b=a>>2  #10000000 =2
print(b) 
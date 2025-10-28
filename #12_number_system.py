#decimal base-10, binary base-2 ,hexadecimal -16 ,octal -8

#program to print decimal to binary value 
x=bin(25)
print(x)  
           #2|25
           #2|12-1
           #2|6-0
           #2|3-0
             #1-0

#program to print binary to decimal value
x=0b11001
print(x)

#program to print decimal to octal
x=oct(25)
print(x)

#program to print decimal to hexadecimal
x=hex(25)
print(x)

#program to print hexadecimal to decimal value
decimal=input("enter value")
x=int(decimal,16)
print(x)

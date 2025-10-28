'''a=5
b=0
try:
    print(a/b)
except Exception as e: # e is just a representation of exception
    print("hey,you cannot divide a number by zero",e)
print("Bye")'''

a=5
b=0
k=int(input("Enter a number"))
print(k)
try:
    print("resource open")
    print(a/b)
except ZeroDivisionError as e: # e is just a representation of exception
    print("hey,you cannot divide a number by zero",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("something went wrong...")

finally: #finally is used for closing files
    print("resource closed")
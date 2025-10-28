nums=[12,15,28,21,26]
for num in nums:
    if num%5==0: #i want divisible by 5 values
        print(num)
        break #i want only first value thats y used break statement
else:
    print("not found") #if the element not availaible then it prints not found
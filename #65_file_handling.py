'''#reading data 

f=open('abc.txt','r')

#print(f.read())

#print(f.readline())


print(f.readline(),end=' ')'''

#writing data
'''f1=open('files','w')
f1.write("hi")
f1.write("good morning")'''

#to append data
'''f1=open('files','a')
f1.write("hello")
f1.write("shiva")'''

f=open('abc.txt','r')
f1=open('files','w')
for data in f:
    f1.write(data)


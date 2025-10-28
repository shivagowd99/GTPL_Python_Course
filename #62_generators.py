def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq #yield gives one by one values,it saves memeory ,yield is not terminates
        n+=1
values = topten()
for i in values:
    print(i)
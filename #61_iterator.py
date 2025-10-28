'''nums = [3,5,4,7]
it=iter(nums)
print(it.__next__()) #it prints next number
print(it.__next__())
print(it.__next__())

for i in nums:
    print(i)'''

class topten():
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration #raise is used for handling exception here otherwise it goes infinite loop
values=topten()
print(next(values))
for i in values:
    print(i)
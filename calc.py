#__name__ == if name is main then only execute main otherwise if importing this main its not execute inside main

'''print("hello" + __name__)'''

'''import demo
print("its time to calculate")'''

def add():
    print("result 1 is",__name__)
def sub():
    print("result 2 is")
    
def main():
    print("in cal main")
    add()
    sub()
if __name__ == "__main__":
    main()
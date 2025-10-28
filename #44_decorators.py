#Decorators- It add extra functionality without changing the original function code.
def decor(p):
    def modified():
        print("good morning shiva")
        p()
        print("Bye")
    return modified  # return the inner function

@decor
def s():
    print("hi")
s()

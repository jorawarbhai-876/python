# print("decorate")


def greet(fx):
    def mfx(*args, **kwargs):
     print("good morning")
     fx(*args, **kwargs)
     print("thnx fo rusing this function")
    return mfx

@greet
def hello():
    print("hello world")

# @greet 
def add (a,b):
    print(a+b)

# @greet(hello)():
hello() 
# greet(add)(1,2) 
add(1,2)  
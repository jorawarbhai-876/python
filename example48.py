x = 10 # global variable

def my_function():
    global x
    x=4
    y = 5 #local variable
    print(y)

my_function() 
print(x)
# print(y) #this will cause error because y is a local variable and is not accesible of the function.
# walrus operator
# a = True
# print(a:= False)

# numbers = [1,2,3,4,5]
# while (n := len(numbers)) > 0:
#     print(numbers.pop())

# new to python 3.8
# assigment expression aka walrus operator assign values to variables as a part of a larger expression

happy = True
print(happy)
print(happy := True)

# food = list()
# while True:
#     food = input("what food do u like?:")
#     if food == "quit":
#        break
    
    # foods.append(food)

food = list()
while(food := input("what food do you like?:"))!= "quit":
    food.append(food)
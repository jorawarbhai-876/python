# 
# REDUCE
from functools import reduce
# list of members
numbers = [1,2,3,4,5]
numbers = [15]
# claculate the sum of the number using the reduce function
def mysum(x,y):
    return x+y
sum = reduce(mysum, numbers)
# print the sum
print(sum) 
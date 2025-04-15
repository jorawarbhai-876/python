class Employe:
 def __init__(self):
  self.__name = "Harry"
 
a = Employe()
# print(a.__name)can not be accessed directly
print(a._Employe__name)#can not be accessed directly
print(a.__dir__())
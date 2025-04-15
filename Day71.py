# dir dict and help
x =[1,2,3]
print(dir(x))
print(x.__add__)

# dict
class person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
  self.version

p = person("john", 30)
print(p.__dict__)

# help
print(help(person))

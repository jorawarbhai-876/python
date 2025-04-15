# Class methods as alterntive constructor
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e = Employee("Harry",12000)
print(e.name)
print(e.salary)

@classmethod
def fromstr(cls,string):
    return cls(string.split("_")[0],string.split("_")[1])

string = "john-12000"
e2=Employee.fromstr(string)
# e2 = Employee(string.split("_")[0],string.split("_")[1])
print(e2.name)
print(e2.salary)

person = Person.from_string("John Doe,30")
print(person.name,person.age) 

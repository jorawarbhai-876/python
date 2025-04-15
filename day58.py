class Person:
    # constructor
    def __init__(self, n, o):
     print("Hey i am a person")
        
     self.name=n
     self.occ=o

   
    
    n="Harry"
    o="developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person("harry", "developer")
b=Person("Divaya", "HR")
# print(a.name)
# a.name="divya"
# a.occupation = "HR"
# a.info()
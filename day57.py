class Person:
    name = "harry"
    occupatuion = "software developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a =Person()
b =Person()
c =Person()
a.name = "shubham"
a.occupation = "Accountant"
print(a.name, a.occupation)
a.info()

b.name ="Nikita"
b.occupation ="HR"

# print(a.name, a.occupation)
a.info()
b.info()
    
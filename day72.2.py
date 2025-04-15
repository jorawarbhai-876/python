class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
 def __init__(self, name, id, lang):
      super().__init__(name, id)  # Call the parent class's constructor
      self.lang=lang
      self.name = name
      self.id = id


    
rohan = Employee("Rohandas", "420")
harry = Programmer("harry", "2335", "python")
print(rohan.name)
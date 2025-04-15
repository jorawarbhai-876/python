#  inheritance in python
class Employe:
 def __init__(self, name, id):
  self.name = name
  self.id = id

def showDetails(self):
 print(f"the name of Employe: {self.id} is {self.name}")

class programmer(Employe):
 def showLanguage(self):
  print(f"the default language is python")
e1 = Employe("Rohan Das", 400)
e1.showDetails()
e2 = programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()  
    
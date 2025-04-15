# instance variable
# class variable 
class Employee:
 companyName = "Apple"
 noOfEmployess = 0
 def __init__(self, name):
  self.name = name
  self.raise_amount = 0.02
  Employee.noOfEmployess +=1
def showDetails(self):
 print(f"the name of Employee is {self.name} and the raise amount in {self.noOfEmployees}sized{self.comapnyName} is {self.raise_amount}")
# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()

Employee.companyName = "google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2 = Employee("Nestle")
emp2.showDetails() 


         
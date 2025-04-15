# class method
# define custom datatype
class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

        @classmethod
        def cahangeCompany(cls, newCompany):
            cls.Company = newCompany
e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)


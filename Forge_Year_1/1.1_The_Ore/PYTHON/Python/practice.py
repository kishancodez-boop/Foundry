# class Employee :
#     Company = "Google"
#     def __init__(self,name):
#         self.name = name 
#     def show(self):
#         print(f"The name of the person is {self.name} and the Company he is working in is {self.Company}")
#     @classmethod
#     def ChangeCompany(cls, NewCompany):
#         cls.Company = NewCompany
# a=Employee(input("Enter the Name of the Employee : "))
# a.show()
# Employee.ChangeCompany(Employee,"Amazon")                                           
# a.show()
# print(Employee.Company)
class s:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def spt(clr,string):
        name,salary=string.split("-")
        return clr(name,salary)
S=s.spt(input("enter the name and salary with - in between : "))
print(S.__dict__)
# print(S.name,"has a salary of",S.salary)
# print(a.name)
# print(a.salary)
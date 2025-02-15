class Person:
    def __init__(self,name,idnum):
        self.name=name
        self.idnum=idnum
    
    def details(self):
        print(f"My name is {self.details}")
    def display(self):
        print(self.name)
        print(self.idnum)
class Employee(Person):
    def __init__(self,name,idnum,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnum)
    
    def details(self):
        print(f"My name is {self.name}")
        print(f"Id number is {self.idnum}")
        print(f"Salary {self.salary}")
        print(f"Post is {self.post}")

emp=Employee("Ankita",1233232,80000,"Developer")
emp.display()
emp.details()
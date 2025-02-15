class Dad:
    def __init__(self,name,occupation,age):
        self.name=name
        self.occupation=occupation
        self.age=age
    
    def details(self):
        print("Name:",self.name)
        print("Occupation:",self.occupation)
        print("Age:",self.age)
    
    def look(self):
        print("Look came from Dad")
class Mom:
    def __init__(self,name,occupation,age):
        self.name=name
        self.occupation=occupation
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Occupation:",self.occupation)
        print("Age:",self.age)

class Child(Dad,Mom):
    def __init__(self,name,age,education,dad_name,dad_age,dad_occupation,mom_name,mom_age,mom_occupation):
        self.name=name
        self.education=education
        self.age=age
        Dad.__init__(self,dad_name,dad_occupation,dad_age)
        Mom.__init__(self,mom_name,mom_occupation,mom_age)
    def business(self):
        print("Child Started new Business ")

obj=Child("Ankita",20,"Btech","Sunil",58,"Professor","Jyoti",50,"HouseWife")
print("--------Dad details--------")
obj.details()
obj.look()
print("--------Mom Details---------")
obj.display()
obj.business()
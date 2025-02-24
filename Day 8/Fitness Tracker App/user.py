class User:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def display(self):
        print(f"------------------\nUser Details: \nName:{self.name}\nAge{self.age}\nWeight{self.weight}\n-------------------")

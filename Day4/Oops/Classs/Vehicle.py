class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display(self):
        print(f"Make {self.make} \nModel:{self.model} \nYear:{self.year}")
    
    def update(self,year):
        self.year=year

car=Vehicle("SUV","Toyata",2004)
car.display()
car.update(2020)
print("--------Updated data---------")
car.display()
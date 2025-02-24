class car:
    def __init__(self,model_name,year):
        self.model_name=model_name
        self.year=year
    def display(self):
        print(f"Model Name:{self.model_name} Year:{self.year}")

c1=car("Toyata",2004)
c1.display()
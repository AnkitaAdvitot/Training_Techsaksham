class Dog:
    attr1="pet"

    def __init__(self,name):
        self.name=name
    
    def speek(self):
        print(f"DOG IS MY LOVE")
Lab=Dog("Tuffy")
print("Lab is a {} ".format(Lab.__class__.attr1))
print("Lab dog name  {} ".format(Lab.name))
Lab.speek()

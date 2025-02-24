from user import *
class Fitness:
    file_data=""
    def __init__(self):
        self.data=[]
    def add(self,date,typeOf,duration):
        self.data.extend([date,typeOf,duration])
        print("Data added")
    def save(self,file_name):
        try:
            f=open(file_name,'a')
            d=" ".join(self.data)
            f.write(d,"\n")
            print("Data stored in file successfuly")
        except FileNotFoundError:
            print("File doesn't exists")
        except PermissionError:
            print("File does not have write permisssion ")
    def view(self,user):
        global file_data
        if self.file_data=="":
            print("Please load the data!!")
        else:
            user.display()
            print(f"--------------{user.name} workout History--------------")
            print(self.file_data)
    def load(self,file_name):
        try:
            global file_data
            f=open(file_name,'r')
            self.file_data=f.read()
            print("Data loaded")
        except FileNotFoundError:
            print("File doesn't exists")
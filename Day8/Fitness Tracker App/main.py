from Fitness import *
from user import *
def main():
    name=input("Enter name ")
    age=int(input("Enter age "))
    weight=int(input("Enter weight "))
    user=User(name,age,weight)
    obj=Fitness()
    while True:
        print("1.Add workut\n2.View Workout\n3.Save Workout\n4.Load Workout\n5.Exit")
        ch=int(input("Enter choice "))
        if ch==1:
            date=input("Enter date ")
            typeOf=input("Enter type of workout ")
            duration=input("Enter duration ")
            obj.add(date,typeOf,duration)
        elif ch==2:
            obj.view(user)
        elif ch==3:
            file=input("Enter file name")
            obj.save(file)
        elif ch==4:
            file=input("Enter file name")
            obj.load(file)
        elif ch==5:
            print("Thank you!!")
            break
        else:
            ch=int(input("Enter valid choice"))

if __name__=="__main__":
    main()
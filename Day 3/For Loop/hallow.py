'''
* * * *
*     *
*     *
* * * *
'''
num=int(input("Enter number "))
for i in range(0,num):
    for j in range(0,num):
        print("* ",end="")
    
    for j in range(0,num-2):
        print("\n*",end="")
        for k in range(0,num+1):
            print(" ",end="")
        print("*")
    for j in range(0,num):
        print("*")
    
    print()
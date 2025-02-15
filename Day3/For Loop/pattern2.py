num=int(input("Enter number"))
n=1
for i in range(0,num):
    for k in range(0,num-i):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
        n+=1
    print()
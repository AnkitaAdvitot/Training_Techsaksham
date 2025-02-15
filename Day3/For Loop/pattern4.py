num=int(input("Enter number"))
n=1
for i in range(0,num):
    for k in range(1,num-i):
        print(end=" ")
    for k in range(0,i+1):
        print(n,end=" ")
        n+=1
    print()

for i in range(num,0,-1):
    for k in range(0,num-i):
        print(end=" ")
    for k in range(0,i):
        n-=1
        print(n,end=" ")
        
    print()


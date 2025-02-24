
#3 2 1 
# 2 1 
#  1
num=int(input("Enter number"))
for i in range(num,0,-1):
    for k in range(0,num-i):
        print(end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    print()
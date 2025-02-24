def isArmstrong(num):
    n=len(num)
    val=int(num)
    sum=0
    temp=val
    while(temp!=0):
        digit=temp%10
        sum+=digit**n
        temp//10
    if(sum==val):
        print(f"{val} is armstrong number")
    else:
        print(f"{val} is not armstrong number")

num=input("Enter number")
isArmstrong(num)
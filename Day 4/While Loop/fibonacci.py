num=int(input("Enter number "))
a=0
b=1
print(a,b,"",end="")
sum=a+b
while sum<=num:
    print(sum,end=" ")
    a,b=b,sum
    sum=a+b

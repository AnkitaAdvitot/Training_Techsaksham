def prime(num):
    flag=True
    for i in range(2,num):
        if(num%i==0):
            flag=False
            print(f"{num} is not prime number")
            break
    if(flag):
        print(f"{num} is prime number")

num=int(input("Enter number"))
prime(num)
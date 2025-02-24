n=int(input("Enter value"))
def isPrime(num):
    flag=True
    for i in range(2,num//2):
        if num%i==0:
            flag=False
            return False
    if flag:
        return True

i=2
count=0
while count!=n:
    if(isPrime(i)):
        print(i,end=" ")
        count+=1
    i+=1
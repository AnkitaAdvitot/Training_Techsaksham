class Palindrome():
    def __init__(self, num):
        self.num=num
        
    def isPalindrome(self):
        temp=self.num
        while temp!=0:
            res=(res*10)+temp%10
            temp//=10
        if res==self.num:
            print(f"{num} is palindrome")
        else:
            print(f"{num} is not palindrome")
class Prime():
    def __init__(self, num):
        self.num=num

    def isPrime(self):
        flag=True
        for i in range(2,self.num):
            if(self.num%i==0):
                print(f"{self.num} is not prime number")
                flag=False
                break
        if(flag):
            print(f"{self.num} is prime number") 
        
class ArmStrong():
    def __init__(self, num):
        self.num=num
    
    def isArmStrong(self):
        str(num)
        n=len(self.num)
        val=int(self.num)
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
class Number(Palindrome,Prime,ArmStrong):
    def __init__(self,num):
        self.num=num
num=int(input("Enter number"))
obj=Number(num)
obj.isArmStrong()
obj.isPalindrome()
obj.isPrime()

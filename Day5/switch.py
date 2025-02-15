def add(*n1,n2):
    
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("Enter your choice"))
n1=int(input("Enter first number "))
n2=int(input("Enter second number "))
if(ch==1):
    res=add(n1,n2)
    print("Addition is ",res)
elif(ch==2):
    res=sub(n1,n2)
    print("Addition is ",res)

elif(ch==3):
    res=mul(n1,n2)
    print("Addition is ",res)
elif(ch==4):
    res=div(n1,n2)
    print("Addition is ",res)
else:
    print("Enter Valid choice")


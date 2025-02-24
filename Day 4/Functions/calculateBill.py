def bill(units):
    total_sum=0
    if(units<=200):
        total_sum=0;
    elif(units>200 and units<=300):
        rem=units-200
        total_sum+=(rem*8)
    elif(units>300 and units<=500):
        rem=units-300
        total_sum+=((100*8)+rem*11)
    elif(units>500):
        rem=units-500
        total_sum+=((100*8)+(200*11)+(rem*14))
    print("total bill is",total_sum)
units=int(input("Enter no. of units "))
bill(units)

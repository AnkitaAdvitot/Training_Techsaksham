str=input("Enter sentence ")
count=0
for i in range(0,len(str)):
    if str[i] in ['a','e','i','o','u']:
        count+=1

print(f"Number of vowels are {count}")
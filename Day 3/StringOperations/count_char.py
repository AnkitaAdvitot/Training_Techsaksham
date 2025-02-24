d=dict()
str=input("Enter sentence ")
for i in range(0,len(str)):
    if str[i] in d:
        c=d[str[i]]
        d.update({str[i]:c+1})
    else:
        d.update({str[i]:1})

for i,j in d.items():
    print(f"{i} {j}")
        
d=dict()
str=input("Enter sentence ")
i=0
while i!=len(str)-1:
    if str[i] in d:
        c=d[str[i]]
        d.update({str[i]:c+1})
    else:
        d.update({str[i]:1})
    i+=1
for i,j in d.items():
    print(f"{i} {j}")
        
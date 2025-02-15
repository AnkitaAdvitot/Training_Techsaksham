l1=[10,298,26,22,1,8]
i=0
n=len(l1)
while i!=n:
    ind=i
    small=l1[i]
    j=i
    while j!=n:
        if l1[j]<small:
            small=l1[j]
            ind=j
        j+=1
    l1[i],l1[ind]=l1[ind],l1[i]
    i+=1
print(l1)

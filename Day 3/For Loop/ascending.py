list=[1,3787,28,98,21]
n=len(list)
for i in range(0,n):
    small=list[i]
    ind=i
    for j in range(i,n):
        if list[j]<small:
            small=list[j]
            ind=j
    list[i],list[ind]=list[ind],list[i]
print(list)
    
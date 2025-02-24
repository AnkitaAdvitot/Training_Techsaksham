str=input("Enter String ")
i=0
l=list()
while i<len(str):
    word=""
    while(i<len(str) and str[i]!=' '):
        word+=str[i]
        i+=1
    l.append(word)
    i+=1
print(l)
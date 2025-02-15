s=input("Enter string ")
word=""
for ch in s:
    if ch>='A' and ch<='Z':
        word+=str(chr(ord(ch)+32))
    else:
        word+=str(chr(ord(ch)-32))
print("Converted String ",word)
def convert(s):
    word=""
    for ch in s:
        if ch>='A' and ch<='Z':
            word+=str(chr(ord(ch)+32))
        else:
            word+=str(chr(ord(ch)-32))
    print("Converted String ",word)

s=input("Enter string ")
convert(s)
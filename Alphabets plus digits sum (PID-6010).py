S=input().strip()
c=0
a='abcdefghijklmnopqrstuvwxyz'

for i in S:
    if(i.isdigit()):
        c+=int(i)

for i in S:
    if(i.isalpha()):
        i=i.lower()
        print(a[(a.index(i)+c)%26],end="")

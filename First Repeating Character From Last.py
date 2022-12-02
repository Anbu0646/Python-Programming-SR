'''
I/P:
abcdexyzbwqpooplj

O/P:
p
'''
#EloisewithJ&O:
s=input().strip()
f=0
for i in range(len(s)-1, 0,  -1):
    for j in range(i-1, 0, -1):
        if(s[i]==s[j]):
            print(s[i], end="")
            f=1
            break
    if(f==1):
        break

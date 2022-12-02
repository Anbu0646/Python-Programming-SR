'''
I/P:
abcdexyzbwqpoolj

O/P:
b
'''
#EloisewithJ&O => @Unfounder
s=input().strip()
f='f'
for i in range (0, len(s) - 1):
    for j in range(i + 1, len(s)):
        if(s[i]==s[j]):
            print(s[i], end="")
            f='a'
            break
    if(f=='a'):
        break

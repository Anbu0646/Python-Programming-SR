'''
I/P:
She is  happy

O/P:
She Is  Happy

'''
#EloisewithJ&O
s=list(input().strip())
s1=""
for i in range(len(s)):
    if i==0:
        s[i]=s[i].capitalize()
    elif (s[i]==" "):
        s[i + 1]= s[i + 1].capitalize()

print(s1.join(s))

S=input().strip()
if len(S)%2:
    f, s = S[:len(S)//2+1], S[len(S)//2:]
else:
    f, s = S[:len(S)//2], S[len(S)//2:]
if f == f[::-1]:
    print(f)
else:
    print(s)

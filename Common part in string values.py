'''
Two string values S1 and S2 are passed as input. The last portion of S1 will be the first portion of S2. The program must print this common part in S1 and S2.

Input Format:

The first line contains S1.
The second line contains S2.

Output Format:

The first line contains the common part.

Boundary Conditions:

Length of S1 and S2 will be from 3 to 100.

Example Input/Output 1:

I/P:

mayday
daybreak

O/P:
day

Example Input/Output 2:

I/P:

bridge
gear

O/P:
ge

#EloisewihJandO
s=input().strip()
s1=input().strip()
l=list(set(s)&set(s1))
for i in l: print(i.sort(), end="")

'''
#EloisewihJandO
s=input()
s=list(s)
s1=input()
s1=list(s1)
k=0
for i in range(int(len(s)/2) - 4, len(s)):
    for j in range(0, len(s1)):
        if k>=len(s1):
            break
        elif (s[i]==s1[k]):
            print(s[i], end="")
        elif (s[i]!=s1[k]):
            break
        k+=1

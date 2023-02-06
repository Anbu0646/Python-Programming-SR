'''
A string S which contains digits as well as non-digits is passed as the input. 
The program has to find the largest even number E that can be formed from the available digits after removing the duplicates(removing repeated digits). 
If it is not possible to form an even number then the program must print -1.

Boundary Condition(s): 1 <= Length of S <= 100 

Input Format:  The first line contains S.
Output Format: The first line contains E or -1. 

Example Input/Output 1: 

Input:  %#36%#%6ab66
Output: 36 

Explanation:  After removing duplicates we have 3 and 6. 
              So 36 is the largest even number that can be formed.

Example Input/Output 2: 

Input:  %e#2393#@i 
Output: 932

Example Input/Output 3: 

Input:  %e#5393#@i 
Output: -1 

Example Input/Output 4: 

Input:  %e#66#@66666i 
Output: 6 

Example Input/Output 5:

Input:  %e#66#@6600666i007
Output: 760

SOLUTION:
'''

s=input()
d=set()
for i in s:
    if i.isdigit():
        d.add(int(i))
dl=sorted(list(d), reverse=True)
ed=0
for j in range(len(d) - 1, -1, -1):
    dd=dl[j]
    if(dd%2==0):
        dl.pop(j)
        dl.append(dd)
        ed=1
        break
if not ed:
    print(-1)
else:
    print(''.join(map(str, dl)))

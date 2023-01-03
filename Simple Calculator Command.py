'''
A string S is passed as input. S will contain two integer values separated by one of these alphabets - A, S, M, D 

where - A or a is for addition 
      - S or s is for subtraction 
      - M or m is for multiplication 
      - D or d is for division 

The program must perform the necessary operation and print the result as the output. (Ignore any floating point values just print the integer result.) 

Input Format:  The first line contains S. 
Output Format: The first line contains the resulting integer value. 

Boundary Conditions: Length of S is from 3 to 100. 

Example Input/Output 1: 

Input:  5A11 
Output: 16 

Explanation:  As the alphabet is A, 5 and 11 are added giving 16. 

Example Input/Output 2: 

Input:  120D6 
Output: 20 

Example Input/Output 3: 

Input:  1405d10 
Output: 140

SOLUTION:
'''

#EloisewithJ
n=input().strip()
c=""
for i in n:
    if i.isalpha():
        c="".join(str(i))
a, b = int(n[:n.index(c)]), int(n[n.index(c)+1:])
if(c=='a' or c=='A'): print(a+b)
elif(c=='s' or c=='S'): print(abs(a-b))
elif(c=='m' or c=='M'): print(a*b)
elif(c=='d' or c=='D'): print(a//b)
else: print("Invalid")

'''
String S which is a palindrome is passed as the input. But just one alphabet A is missing in S. The program must print the missing alphabet A. 

Note: The FIRST alphabet of S will always be present. 

Input Format:  The first line contains S. 
Output Format: The first line contains the missing alphabet A.

Boundary Conditions: The length of the input string S is between 3 to 100. 
The FIRST alphabet of S will always be present. 

Example Input/Output 1: 

Input:  malayaam 
Output: l 

Example Input/Output 2:

Input:  abcddcb 
Output: a

SOLUTION:
'''

#1899withonly0
s=input().strip()
s1=list(s)
l1=len(s) -1
for i in range(len(s)):
    if s1[i]!=s1[l1]:
        if(s1[i]==s1[l1 - 1] and i!=l1 - 1):
            print(s1[l1], end="")
            break
        else:
            print(s1[i], end="")
            break
    l1-=1

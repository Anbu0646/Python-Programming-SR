'''
A str‌ing S (only alphabets) is passed as input. The printed output should contain alphabets in odd positions in each word in uppercase and alphabets in even positions in each word in lowercase. 

Input Format:  The first line will contain S. 
Output Format: The first line will contain the resultant string value based on the conditions provided. 

Boundary Conditions: Length of S is from 3 to 100. 

Example Input/Output 1: 

Input:  tREE GiVES us fruiTS 
Output: TrEe GiVeS Us FrUiTs 

Example Input/Output 2: 

Input:  FLoweR iS beauTIFUL
Output: FlOwEr Is BeAuTiFuL

SOLUTION:
'''

s=list(input().split(" ")
for i in range(0, len(s)):
    l=list(s[i])
    for j in range(0, len(l)):
        if (j%2==0): print(l[j].upper(), end="")
        else: print(l[j].lower(), end="")
    print(" ",end="")

'''
Recently a security committee decided to enforce the following rules when an employee creates/changes his/her password. 

- The password must contain atleast one special character among # ! _ $ @ 
- The password must contain atleast two numbers
- The password must contain atleast one upper case alphabet and one lower case alphabet.
- The password must have a minimum length of 8.
- The password must have a maximum length of 25. 

The program must accept a given password string P as input and check for these rules and output VALID or INVALID.

Boundary Conditions: Length of P is from 2 to 50. 

Input Format:  First line will contain the string value of the password P 
Output Format: VALID or INVALID based on the check performed by the program by applying the rules.

Example Input/Output: 

Example 1:  
Input:  kiC_3b0x3r 
Output: VALID 

Example 2:

Input:  m@d31nindia 
Output: INVALID 

Explanation: No alphabet in uppercase. 

Example 3: 

Input:  M1kT!s0
Output: INVALID 

Explanation: Minimum length must be 8

SOLUTION:
'''

s=input().strip()
SP, D, U, L, l = 0, 0, 0, 0 , len(s)
for i in s:
    if i.isupper(): U+=1
    if i.islower(): L+=1
    if i.isdigit(): D+=1
    if (i=='#' or i=='@' or i=='!' or i=='_' or i=='$'):  SP+=1
print("VALID" if(D>=2 and L>=1 and U>=1 and SP>=1 and (l>=8 and l<=25)) else "INVALID")

'''
A string (with only alphabets) S is passed as input. The program should print the alphabets in the string in descending order. 
Assume all alphabets will be in lower case. 

Boundary Conditions: The length of string S is between 2 and 100. 

Example input and output: 

If the input is "cake", the output should be "keca".

If the input is "innovation", the output should be "vtonia" (n or o or i should not be repeated).

SOLUTION:
'''

s=input().strip()
print(*sorted(set(s))[::-1], sep="")

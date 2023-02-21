'''
Two string values S1 and S2 are passed as input. The program must print the count of common characters in the strings S1 and S2. Assume the alphabets in S1 and S2 will be in lower case. 

Input Format:  First line will contain the value of string S1 Second line will contain the value of string S2 
Output Format: First line will contain the count of common alphabets. 

Boundary Conditions: Length of S1 and S2 will be from 3 to 100. 

Sample Input/Output: 

Example 1: 

Input:  china 
        india 
Output: 3 

Explanation: The common characters are i,n,a 

Example 2: 

Input:  energy 
        every 
Output: 3 

Explanation: The common characters are e,r,y

SOLUTION:
'''

from collections import Counter
s1=input().strip(); s2=input().strip()
s3=Counter(s1)&Counter(s2)
print(sum(s3.values()))

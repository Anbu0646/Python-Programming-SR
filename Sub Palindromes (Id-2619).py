'''
Given a string s, the program must print the count of sub palindromes (with a minimum length of two characters) in the string s. 

Boundary conditions: length of the string is between 2 and 200. 

Input format:  First line will contain the string value s. 
Output format: First line will contain the integer which represents the count of sub palindromes in the string s. 

Sample input/output: 

Example 1: 

Input:  everest 
Output: 2 

Explanation: the sub palindromes are eve, ere 

Example 2: 

Input:  abccbaab 
Output: 5 

Explanation: the sub palindromes are cc, bccb, aa, baab, abccba


Solution:
'''

s=input()
c=0

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if(s[i]==s[j]):
            d=0
            for k, l in zip(range(i, j+1), range(j, i-1, -1)):
                if(s[k]==s[l]):
                    d+=1
            if(d==(j - i)+1):
                c+=1

print(c)

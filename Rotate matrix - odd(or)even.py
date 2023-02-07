'''
The program is provided with one or more strings separated by a comma, where each string is associated with an integer following it after a colon (:). 
If the sum of the squares of the digits of the associated integer is even then rotate the string right by one position. 
If the sum of the squares of the digits of the associated integer is odd then rotate the string left by two positions.

Boundary Condition(s): 1 <= Count of String Values <= 20 

Input Format:  The first line contains the string values separated by a comma. 
Output Format: The lines contain the string values rotated based on the given conditions. 

Example Input/Output 1: 

Input:  abcde:234,pqrs:246 
Output: cdeab spqr 

Explanation:  For abcde, the integer is 234. The sum of squares of the digits is 4+9+16=29 which is odd. 
              So abcde is rotated left by two positions resulting in cdeab. 
              For pqrs, the integer is 246. The sum of squares of the digits is 4+16+36=56 which is even. 
               So abcde is rotated right by one position resulting in spqr.

Example Input/Output 2:

Input:  xyz:193 
Output: zxy

SOLUTION:
'''

s=input()
s1=s.split(',')
for i in range(len(s1)):
    s2=s1[i].split(':')
    d=int(s2[1])
    c=0
    while(d>0):
        c+=(d%10)*(d%10)
        d=d//10
    l=len(s2[0])
    if(c%2==0):
        print(s2[0][l-1:]+s2[0][:l-1])
    else:
        print(s2[0][2:]+s2[0][:2])

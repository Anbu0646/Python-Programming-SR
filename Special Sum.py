'''
The program must accept N integers as the input and print the count C of combinations of K integers which add upto a special sum S which is an integer value. 

Boundary Condition(s): 1 <= K <= N <= 25

Input Format:  The first line contains N, K and S separated by a space. The second line contains N integer values separated by a comma. 
Output Format: The first line contains C.

Example Input/Output 1: 

Input:   6 4 0
        -1,1,0,0,2,-2 
Output: 3 

Explanation:  As K is 4 and S is 0, we need to consider the combination of four integers. 
              (-1,1,2,-2), (0,0,1,-1), (0,0,-2,2) are the combinations which add upto S (as S is 0).

Example Input/Output 2: 

Input:  6 4 3 
        5,1,0,0,2,-2 
Output: 2

SOLUTION:
'''

from itertools import combinations
n=list(map(int, input().strip().split()))
a, b, c, d = n[0], n[1], n[2], 0
q=list(map(int, input().split(",")))
l=list(combinations(q, b))
for i in l:
    s=sum(i)
    if s==c:
        d+=1
print(d)

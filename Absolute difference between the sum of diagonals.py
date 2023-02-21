'''
You are given a square matrix of size N×N. Calculate the absolute difference of the sums across the two main diagonals. 

Boundary Condition(s): 2 <= N <= 20

Input Format:  The first line will contain the value of N.
               The next N lines will contain the N values separated by one or more spaces. 
Output Format: The absolute difference of the sums across the two main diagonals.

Example Input/Output 1: 

Input:  2 
        10 9
        4  22 
Output: 19

Explanation: The sum along the first main diagonal is 10+22 = 32. 
             The sum along the second main diagonal is 4+9=13. 
             The absolute difference is 32-13= 19.

Example Input/Output 2:
Input:  2 
        -10 6 
         4 -22 
Output: 22

SOLUTION:
'''

n=int(input())
m=[list(map(int, input().split())) for i in range(n)]
s1, s2 = 0, 0
for j in range(n):
    for k in range(n):
        if(j==k):   s1+=m[j][k]
        if(j==n - k - 1):   s2+=m[j][k]
print(abs(s1+s2) if (s1<0 and s2>0) else abs(s1 - s2))

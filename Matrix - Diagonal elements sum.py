'''
You are given a square matrix of size N×N. Calculate the sum of the integers present in the two main diagonals.

Input Format:  The first line will contain the value of N. 
               The next N lines will contain the N values separated by one or more spaces. 
Output Format: The sum of the integers present in the two main diagonals. 

Boundary Conditions: 2 <= N <= 20

Example Input/Output 1: 

Input:  2 
        10 9 4 22 
Output: 45 

Explanation: The sum is = 10+22+9+4 = 45 

Example Input/Output 2: 

Input:  3 
        5 10 11
        79 6 12 
        9 21 45
Output: 76

Explanation: The sum is = 5+6+45+11+9 = 76. As 6 is common for both the diagonals it must be counted only once when finding the sum.

SOLUTION:
'''

n=int(input())
m=[list(map(int, input().split())) for i in range(n)]
s=0
for j in range(n):
    for k in range(n):
        if(j==k or j==n - k - 1):
            s+=m[j][k]
print(s)

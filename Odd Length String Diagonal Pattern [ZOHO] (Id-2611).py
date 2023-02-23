'''
An odd length string S of length L is passed as the input. The program must print the string S as two diagonals as shown in the example Input/Output below. 

Input Format:  The first line will contain S.
Output Format: L lines will contain the pattern as shown in the example Input/Output below. 

Boundary Conditions: Length of S is from 3 to 51. 

Example Input/Output 1: 

Input:  cry 
Output: c y 
         r 
        c y 


SOLUTION:
'''
s=input().strip()
l=list(s)

for i in range(len(l)):
    k=len(l) - i - 1
    for j in range(len(l)):
        if i==j:
            print(l[j], end="")
        elif j==k:
            print(l[j], end="")
        else:
            print(" ", end="")
    print()

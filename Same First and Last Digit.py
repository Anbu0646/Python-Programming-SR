'''
The program must accept N integers as the input. The program must print the integers which are having the same first and last digits. If there is no such integer then the program must print -1 as the output. 

Boundary Condition(s): 1 <= N <= 1000 
                       10 <= Each integer value <= 10^8 
                       
Input Format:  The first line contains the value of N. 
               The second line contains N integer values separated by space(s). 
               
Output Format: The first line contains the integer values separated by a space. 

Example Input/Output 1: 

Input:  6 
        959 7829 6366 50 525 44 
Output: 959 6366 525 44 

Explanation:  The first integer is 959. The first digit and the last digit are the same. so 959 is printed. 
              The second integer is 7829. The first digit and the last digit are not the same. so 7829 is not printed. 
              The third integer is 6366. The first digit and the last digit are the same. so 6366 is printed. 
              The fourth integer is 50. The first digit and the last digit are not the same. so 50 is not printed. 
              The fifth integer is 525. The first digit and the last digit are the same. so 525 is printed. 
              The sixth integer is 44. The first digit and the last digit are the same. so 44 is printed. 
              Hence the output is 959 6366 525 44 
              
Example Input/Output 2: 

Input:  5 
        419 327 268 230 132 
        
Output: -1

SOLUTION:
'''

#1899withonly0
n=int(input())
l=list(map(str, input().split()))
c=0
for i in l:
    f=i[0]
    l=i[-1]
    if(f==l):
        print(i, end=" ")
        c=1
if(c==0): print("-1")

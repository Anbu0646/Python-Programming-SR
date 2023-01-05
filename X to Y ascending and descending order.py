'''
The program must accept two integers X and Y as the input. The program must print the even integers from X to Y. 
If X is less than Y then the program must print them in ascending order else the program must print them in descending order. 

Boundary Condition(s): 1 <= X, Y <= 1000 

Input Format:  The first line contains X and Y separated by space. 
Output Format: The first line contains integers separated by space. 

Example Input/Output 1: 

Input:  12 20 
Output: 12 14 16 18 20

Example Input/Output 2: 

Input:  30 21 
Output: 30 28 26 24 22

SOLUTION:
'''
#1899withonly0
x, y = map(int, input().split())
l=[]
d=[]
for i in range(x, y+1, 1):
    if(i%2==0): l.append(i)
for j in range(y, x+1, 1):
    if(j%2==0): d.append(j)
if(x<y):    print(*l)
else:
    d.reverse()
    print(*d)

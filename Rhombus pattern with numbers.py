'''
Input:  5
Output: - - - - * * * * * 
        - - - * 1 2 3 * 
        - - * 4 5 6 * 
        - * 7 8 9 * 
        * * * * *
        
SOLUTION:
'''

r=int(input())
c=1
for i in range(1, r+1):
    for j in range(1, r-i+1): print(end="- ")
    for j in range(1,r+1):
        if i==1 or j==1 or j==r or i==r:
            print('*',end=" ")
        else:
            print(c,end=" ")
            c+=1
    print()

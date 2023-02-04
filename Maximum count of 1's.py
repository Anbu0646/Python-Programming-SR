'''
An array of N elements is passed as input to the program. The elements values are either 0 or 1. 
Exactly one operation can be performed on any one of the subarray so as to invert all the bits (changing 0 to 1 and 1 to 0) in the selected subarray. 
The minimum size of the subarray to be selected is 1 and the maximum size is N. 
The program must print the maximum number of 1s that you can get by doing the operation described above. 

Boundary Condition(s): 1 <= N <= 100 

Input Format:  The first line contains N. The second line contains N integers separated by a space.
Output Format: The first line contains the maximum count of 1s. 

Example Input/Output 1: 

Input:  6
        1 0 0 1 0 1
Output: 5 

Explanation:  When we invert the sub-array from index 1 to 2 (that is second and third elements) we get 1 1 1 1 0 1.
              Here we get the maximum count of 1s which is 5. 

Example Input/Output 2:

Input:  9 
        1 0 0 1 0 0 1 1 1 
Output: 8

SOLUTION:
'''

n=int(input())
l=list(map(int, input().strip().split()))[:n]
c=0
for i in range(n):
    for j in range(i, n):
        a=""
        for k in range(i):
            a+=str(l[k])
        for m in range(i, j+1):
            if(l[m]==1):
                a+='0'
            else:
                a+='1'
        for o in range(j+1, n):
            a+=str(l[o])
        mx=0
        for p in range(len(a)):
            if(a[p]=='1'):
                mx+=1
        c=max(c, mx)
print(c)

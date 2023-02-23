'''
An array of N integers with non-zero values is passed as the input to the program. The program must print another array of size N where value at each index will be the product of all values in the input array except the value at that index in the input array. 

Input Format:  The first line will contain N integers separated by a space. 
Output Format: The first line will contain N integers separated by a space. 

Boundary Conditions: The length of the input containing N integers will be from 3 to 100. 
		     The integer values will be from 1 to 100. 

Example Input/Output 1: 

Input:  1 2 3 4 5 
Output: 120 60 40 30 24 

Example Input/Output 2: 

Input:  10 5 4 
Output: 20 40 50 

Example Input/Output 3: 

Input:  21 100 
Output: 100 21


Solution:
'''

l=[int(i) for i in input().split()]
for i in range(len(l)):
    mul=1
    for j in range(len(l)):
        if(i!=j):
            mul=mul*l[j]
    print(mul, end=" ")
    
'''
from functools import reduce
from operator import mul
l=[int(i) for i in input().split()]
v=reduce(mul, l)
l1=[v//i for i in l]
print(*l1)
'''

'''
Two cans are with capacity X and Y liters. The program must determine the number of steps required to obtain exactly Z litres of liquid in one of the cans. 
At the beginning both cans are empty. 

The following operations are counted as "steps". 

- emptying a vessel, - filling a vessel, - pouring liquid from larger can to the smaller, without spilling, until one of the cans is either full or empty. 

If it is not possible to obtain Z liters exactly then the output must be -1.

Boundary Conditions:  0 < X <= 100 
                      0 < Y <= 100 
                      0 < Z <= 100 

Input Format:  First line will contain the value of X Second line will contain the value of Y Third line will contain the value of Z 
Output Format: The number of steps required as an integer. If it is not possible to obtain Z liters then the output is -1. 

Sample Input/Output: 

Example 1:  

Input:  5 
        2
        3 
Output: 2 

Explanation: Here X=5, Y=2 
            Step 1: Pour 5 liters of liquid into 5 liter can 
            Step 2: Pour 2 liters from 5 liter can into 2 liter can. 
            Now the 5 liter can will have 3 liters which is Z.
            Hence 2 steps are required. 

Example 2: 

Input:  2 
        3 
        4 
Output: -1

Explanation: Z is greater than X and Y. Hence it is not possible to have 4 liters in any one of the cans. Hence output is -1.
 
SOLUTION:
'''

x=int(input()); y=int(input()); z=int(input())
a, c = y, 0

while (1):
    
    if(x>y and x>z):
        b=x - a
        c+=2
    
        if(b==z):   
            print(c)
            break
        elif(x>b and b>z):  
            a+=y
        else: 
            print(-1)
            break
        
    else:
        print(-1)
        break

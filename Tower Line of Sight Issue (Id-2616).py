'''
Four towers A, B, C, D are to be erected. Tower A is to communicate with tower C. Tower B is to communicate with tower D. Line of sight issue can occur under the following conditions - when tower B or D is in the straight line connecting A and C - when tower A or C is in the straight line connecting B and D The program must accept the co-ordinates of all four towers and print yes or no depending on whether Line of sight issue will occur or not. 

Input Format:  The first line will contain X and Y co-ordinates of tower A separated by a space. 
	       The second line will contain X and Y co-ordinates of tower B separated by a space. 
               The third line will contain X and Y co-ordinates of tower C separated by a space. 
               The fourth line will contain X and Y co-ordinates of tower D separated by a space 
Output Format: The first line will contain yes or no (smaller case) 

Boundary Conditions: The value of the co-ordinates will be from -500 to 500. 

Example Input/Output 1: 

Input:  0 0 
	0 -2
	2 0
	0 2 
Output: yes 

Example Input/Output 2: 

Input:  0 0
	0 -2 
	2 0 
	0 -5 
Output: no


Solution:
'''

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

f1, f2 =0, 0

if( ( ((b1<=a1 and b2<=c1) or (b1>=c1 and b1>=a1)) and ((b2<=a2 and b2<=c2) or (b2>=a2 and b2>=c2))) and (((d1<=a1 and d1<=c1) or (d1>=c1 and d1>=a1)) and ((d2<=a2 and d2<=c2) or (d2>=a2 and d2>=c2) ) )):
    f1=1
if( ( ((a1<=b1 and a1<=d1) or (a1>=b1 and a1>=d1)) and ((a2<=b2 and a2<=d2) or (a2>=b2 and a2>=d2))) and (((c1<=b1 and c1<=d1) or (c1>=b1 and c1>=d1)) and ((c2<=b2 and b2<=d2) or (c2>=b2 and c2>=d2) ) )):
    f2=1

print("no" if(f1==1 and f2==1) else "yes")

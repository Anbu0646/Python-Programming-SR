'''
The program must accept N integers as the input. For each integer, the program must print the prime digit(s) sorted in ascending order. 
If the integer does not have any prime digit then the program must print -1 for that integer as the output. 

Boundary Condition(s):  1 <= N <= 1000 

Input Format:  The first line contains the value of N. 
               The second line contains N integers separated by a space.
Output Format: The first line contains -1 or the integers of prime digit(s) separated by a space.

Example Input/Output1: 

Input:  6 
        61165 65613 48469 78435 98716 7583249 
Output: 5 35 -1 357 7 2357 

Explanation: 61165 is sorted as 11566. The prime digit is 5. So 5 is printed.
             65613 is sorted as 13566. The prime digits are 35. So 35 are printed. 
             48469 is sorted as 44689. There is no prime digit. So -1 is printed. 
             78435 is sorted as 35487. The prime digits are 357. So 357 are printed. 
             98716 is sorted as 16789. The prime digit is 7. So 7 is printed. 
             7583249 is sorted as 2345789. The prime digits are 2357. So 2357 are printed. 

Example Input/Output2: 

Input:  4 
        248 948 6840 864 
Output: 2 -1 -1 -1

SOLUTION:
'''

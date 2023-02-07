'''
The program must accept an integer N as the input. 
The program must multiply the first half of the digits in N as product. 
Then the program must add the second of the digits as sum. 
Finally, the program must add and print the values of sum and product as the output.

Note: Number of digits in N is always even. 

Boundary Condition(s): 1 <= N < 10^8

Input Format:  The first line contains N. 
Output Format: The first line contains the integer based on the given condition. 

Example Input/Output 1: 

Input:  547856
Output: 159 

Explanation:  The first half of the digits are 5 4 8 which are multiplied 5x4x7 = 140. 
              The second half of the digits are 8 5 6 which are added 8 + 5 + 6 = 19. 
              The sum and product are added 140 + 19 = 159 which is printed as the output.

Example Input/Output 2: 

Input:  1234 
Output: 9

SOLUTION:
'''

s = input().strip()
a, b = 1, 0 
for i in range(0, len(s)//2):
    a *= int(s[i])
for i in range(len(s)//2, len(s)):
    b += int(s[i])
print(a + b)

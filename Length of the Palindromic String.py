'''
The program must accept a string S containing digits as the input. The program must check whether it is a palindrome or not. 
If it is not a palindrome, reverse the string, add it to the original string and check again. 
The program must repeat the process until the string becomes palindrome. 
Finally, the program must print the length of the palindromic string. 

Boundary Condition(s): 1 <= Length of S <= 10^8 

Input Format:  The first line contains S. 
Output Format: The first line contains the length of the palindromic string. 

Example Input/Output 1: 

Input:  145 
Output: 3 

Explanation:  The given string is 145, it is not a palindrome.
              After reversing and adding, 145+541 = 686.
              The length of the palindromic string 686 is 3. 
              Hence the output is 3 

Example Input/Output 2: 

Input:  1 
Output: 1

SOLUTION:
'''

def lops(s):
    x=int(str(s)[::-1])
    if(x==s):
        return x
    return lops(x+s)
s=int(input())
if(s>=1 and s<=9):
    print(1)
else:
    print(len(str(lops(s))))

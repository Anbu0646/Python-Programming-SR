'''
The program must accept a lower case alphabet as the input. The program must print from the given alphabet to the next occurring vowel as the output. 

Note: If there is no vowel after the given alphabet then the program must print till z as the output. 

Input Format:  The first line contains the alphabet. 
Output Format: The first line contains alphabets without space. 

Example Input/Output 1: 

Input:  g 
Output: ghi 

Explanation: The next occurring vowel after g is i. So ghi is printed as the output. 

Example Input/Output 2: 

Input:  e 
Output: efghi

SOLUTION:
'''

#1899withonly0
c=input().strip()
a='abcdefghijklmnopqrstuvwxyz'
v='aeiou'
k=a.index(c)
l=a[k:]
for i in l: 
    if i in v:
        print(i, end="")
        break
    else:
        print(i, end="")

'''
An expression E is passed as an input to the program. 
The expression will contain three numbers A, B and C, one equal symbol and one of the mathematical operators + - * / 
But the given mathematical operator is incorrect and hence the expression is not valid. 
Hence the program must identify the correct operator and print that as the output. 

Input Format:  First line will contain the expression E 
Output Format: First line will contain the correct mathematical operator 

Sample Input/Output: 

Example 1: 

Input:  5-4=20 
Output: * 

Explanation:  Only 5 multiplied with 4 gives 20.  Hence - must be replaced with *. 
     
Example 2: 

Input:  999+9=111 
Output: / 

Explanation: Only 999 divided by 9 gives 111. Hence + must be replaced with /.

SOLUTION:
'''
#1899withonly0
e=input()
t, a = map(str, e.split("="))
o="+-*/"
for i in range(len(t)):
    if(t[i] in o):
        n1, n2 = t[:i], t[i+1:]
for i in o:
    if(eval(n1+i+n2)==int(a)):
        print(i)
        break

'''
A string S is passed as the input. Two words W1 and W2 which are present in the string S are also passed as the input. The program must find the minimum distance D between W1 and W2 in S (in forward or reverse order) and print D as the output. 

Input Format:  The first line will contain S. 
               The second line will contain W1. 
               The third line will contain W2. 
Output Format: The first line will contain D - the minimum distance between W1 and W2 in S. 

Boundary Conditions: Length of S is from 5 to 200. 

Example Input/Output 1: 

Input:  the brown quick frog quick the the quick 
Output: 1 

Explanation: quick and the are adjacent as the last two words. Hence distance between them is 1. 

Example Input/Output 2: 

Input:  the quick the brown quick brown the frog quick frog 
Output: 3


Solution:
'''

s1=input().strip(); s2=input().strip(); s3=input().strip()

if(s3==s2):
    print(1)
    
else:
    w=s1.split(" ")
    l=len(w)
    dis=l+1
    
    for i in range(l):
        if(w[i]==s2 or w[i]==s3):
            las=i
            break
    
    for i in range(l):
        if(w[i]==s2 or w[i]==s3):
            if(w[las]!=w[i]):
                if(i - las)<dis:
                    dis=i - las
                    las=i
            else:
                las=i

    print(dis) 

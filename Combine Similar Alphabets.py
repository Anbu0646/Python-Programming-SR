'''
The program must accept a string S and combine the similar alphabets (lower and upper case are similar) based on their order of occurrence. 
Then the program must form a new string M by alternating the elements from first and last. 

Boundary Condition(s): 1 <= Length of S <= 1000 

Input Format:  The first line contains S. 
Output Format: The first line contains M. 

Example Input/Output 1: 

Input:  HelLoWOrld 
Output: dWerHoOlLl 

Explanation:  'd', 'e', 'H', 'lLl', 'oO', 'r', 'W' are the grouped similar alphabets. 
               So d and W are printed first. Then e and r are printed. 
               Then H and oO are printed. 
               Then lLl is printed.
               
Example Input/Output 2: 

Input:  tapa 
Output: aatp 

Example Input/Output 3: 

Input:  u
Output: u

SOLUTION:
'''

k=input()
u=sorted(set(k.upper()))
l=[], n=""
for i in range(len(u)):
    m=""
    for j in k:
        if u[i]==j.upper():
            m+=j
    l.append(m)
i, j = 0, len(l) - 1
while (i<=j):
    if(i==j):
        n+=l[i]
    else:
        n+=l[i]+l[j]
    i+=1
    j-=1
print(n)

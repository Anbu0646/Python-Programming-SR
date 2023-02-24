'''
INPUT 1:
909

OUTPUT 1:
919

INPUT 2:
121

OUTPUT 2:
131

SOLUTION:
'''

n=int(input())
while(1):
    n+=1
    ns=str(n).strip()
    nsr=ns[::-1]
    if(ns==nsr):    
        print(nsr)
        break

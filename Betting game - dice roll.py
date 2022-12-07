'''
I/P:
      1 4 3
      10
      30
O/P:
      -10
'''
#Unfounder
n=input().split()
x=int(input())
y=int(input())
o=0
e=0
for i in n:
    if int(i)%2!=0:
        o=o+x
    else:
        e=e+y
        
print(o-e)

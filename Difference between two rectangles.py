'''

I/P:
100000 80000
100 80

O/P:
0.00

'''
#EloisewithJandO
a,b = map(int, input().split()) 
c,d = map(int, input().split())
e=a/5
f=e//c
g=b/5
h=g//d
print('%.2f'%abs(h-f))

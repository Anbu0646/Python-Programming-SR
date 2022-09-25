# Accept a list of M and N integers as the input. The program must print the common unique integers between the two lists M and N in the order given in M. If there is no common unique integer then the program must print "Invalid" as the output.
# Solution:
a, b= map(int,input().split())
if a!=0 and b!=0:
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
else:
    print("Invalid")
    exit(0)
k = 0
l=[]
for i in c:
    if i in d and i not in l:
        k = 1
        print(i,end=' ')
        l.append(i)
if k==0:
    print("Invalid")

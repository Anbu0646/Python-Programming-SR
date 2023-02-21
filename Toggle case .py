'''
Input1:
gooD EvenIng

Output1:
GOOd eVENiNG

Input2:
gooD$%Thou GH$!@t

Output2:
GOOd$%tHOU gh$!@T
'''
s=input().strip()
for i in s:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower:
        print(i.upper(), end="")
    else:
        print(i, end="")

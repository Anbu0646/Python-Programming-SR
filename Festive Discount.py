'''
In a shop, discounts were provided as below. - If the label price of an item is more than Rs.400, then the discount is 20%. 
                                             - If the label price of an item is more than Rs.500, then the discount is 25%. 
                                             - If the label price of an item was more than or equal to Rs.1000, then the discount is 50%. 
                                             - Finally if the total purchase amount after discount is more than Rs.2000 a further discount of Rs.100 is provided. 
The label prices of the items purchased will be provided as input. The program has to calculate the final price payable by the buyer (customer). 

Boundary Conditions: Number of items bought will be from 1 to 20. 

Input Format:  First line will contain the number of items (N) Next N lines will contain the label price of N items.
Output Format: The final price payable by the buyer rounded off to two decimal places. 

Sample Input/Output: 

Example 1: 

Input:  3 
        1000 
        1200 
        400 
Output: 1500.00

Explanation: 1000, 1200, 400 after discount becomes 500, 600, 400 (20% discount is applicable only if the label price is more than Rs.400)
             Hence net payable amount = 500+600+400 = 1500 

Example 2: 

Input:  5 
        450 
        500 
        2000 
        1600 
        300
Output: 2760.00 

Explanation: After discount the selling price of items are 360, 400, 1000, 800, 300. Net amount = 2860. 
             As 2860 > 2000, a further discount of 100 is provided and hence output is 2760.00

SOLUTION:
'''

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
s=0
for j in range(n):
    if(l[j]>400 and l[j]<=500):
        s+=l[j]-((l[j]*20)//100)
    elif(l[j]>500 and l[j]<1000):
        s+=l[j]-((l[j]*25)//100)
    elif(l[j]>=1000):
        s+=l[j]-((l[j]*50)//100)
    else:
        s+=l[j]
print("{:.2f}".format(float(s - 100.0)) if (s>2000) else "{:.2f}".format(float(s)))

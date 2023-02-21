'''
The day corresponding to the first date of a given month is provided as input to the program. Then a specific date D of the month is provided. 
The program must print the day (one among MON,TUE, WED, THU, FRI, SAT, SUN) of the date D. 

Input Format:  First line will contain the day (one among MON,TUE, WED, THU, FRI, SAT, SUN) of the first date of the month. 
               Second line will contain the value of the date D as an integer value. 
Output Format: First line will contain the day of the date D 

Sample Input/Output: 

Example 1: 

Input:  MON 
        10 
Output: WED

Explanation:  If it is Monday on 1st of the month, then 10th of the month will be a Wednesday. Hence WED is printed.

Example 2: 

Input:  FRI 
        24
Output: SUN 

Explanation: If it is Friday on 1st of the month, then 22nd will also be a Friday. Hence 24th of the month will be a Sunday. Hence SUN is printed.

SOLUTION:
'''

day=input().strip()
date=int(input())
week=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
if(day in week):
   f=date+week.index(day)
f=f%7
if(f==0):   print('SUN')
elif(f==1):   print('MON')
elif(f==2):   print('TUE')
elif(f==3):   print('WED')
elif(f==4):   print('THU')
elif(f==5):   print('FRI')
elif(f==6):   print('SAT')

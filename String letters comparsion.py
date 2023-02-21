'''
Two string values S1 and S2 are passed as input. The program must check if both S1 and S2 contain the same unique set of letters and print YES or NO.
Assume all the letters (alphabets) are in smaller case. 

Boundary Conditions: Length of S1 is from 2 to 100 Length of S2 is from 2 to 100 

Input Format:  First line will contain the string value of S1 Second line will contain the string value of S2 
Output Format: YES or NO depending on if both S1 and S2 contain the same set of unique letters. 

IMPORTANT: Please note that the output is CASE SENSITIVE. Hence print YES or NO (instead of yes or no)

Sample Input/Output: 

Example 1: 

Input:  read 
        dear 
Output: YES

Explanation: Both S1 and S2 are formed using the letters - a d e r 

Example 2:
Input:  record 
        decoder
Output: YES 

Explanation: Both S1 and S2 are formed using the letters - c d e o r 

Example 3: 

Input:  energy 
        synergy 
Output: NO 

Explanation: S2 has additional letter - s in it.

SOLUTION:
'''

s1=input().strip(); s2=input().strip()
print("YES" if (sorted(set(s1))==sorted(set(s2))) else "NO")

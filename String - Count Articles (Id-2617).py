'''
A string S is passed as the input. The program must print the number of articles (a, an and the) in S. The string S passed as the input NEED NOT be correct grammatically. 

Input Format:  The first line will contain S 
Output Format: The first line will contain the count of articles in S. 

Boundary Conditions: The length of the string S will be from 3 to 1000. 
                     Each word in S will not be more than 100 characters. 

Example Input/Output 1: 

Input:  I went to a movie yesterday along with an old man. 
Output: 2
 
Example Input/Output 2: 

Input:  In 1885 it was banished from the shelves of the Concord Public Library, an act that attracted a lot of publicity and discussion in the press. It is still frequently in the news, as various schools and school systems across the country either ban it from or restore it to their classrooms. The texts and illustrations below attempt to capture both the novel's achievement and some aspects of its controversiality.
Output: 8


Solution:
'''
s=input().split()
c=s.count('a')+s.count('an')+s.count('the')+s.count('a,')+s.count('an,')+s.count('the,')+s.count('a.')+s.count('an.')+s.count('the.')
print(c)

import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = list()
    def pushCharacter(self,val):
            self.stack.append(val)
        
    def enqueueCharacter(self,val):
            self.queue.insert(0,val)
    def popCharacter(self):
        char1 = self.stack.pop()
        return char1
    def dequeueCharacter(self):
        char2 = self.queue.pop()
        return char2
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    

class Solution(object):
    def isPalindrome(self, x):
        
        newx=str(x)
        if(newx==newx[::-1]):
            return True
        else:
            return False
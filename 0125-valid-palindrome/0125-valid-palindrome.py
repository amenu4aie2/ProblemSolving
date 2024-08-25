class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalnum():
                x+=i
        x=x.lower()
        i,j=0,len(x)-1
        while i<j:

            if(x[i]==x[j]):
                i+=1
                j-=1
            else:
                return False
        return True

        

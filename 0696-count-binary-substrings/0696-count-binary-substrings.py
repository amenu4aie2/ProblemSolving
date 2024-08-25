
class Solution:
    
    def countBinarySubstrings(self, s: str) -> int:
        curcount=1
        prevcount=0
        count=0
        

        for i in range(1,len(s)):
            if(s[i-1]==s[i]):
                curcount+=1
            else:
                count+=min(prevcount,curcount)
                prevcount=curcount
                curcount=1
        return count+min(prevcount,curcount)
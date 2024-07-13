from itertools import takewhile
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs=defaultdict(int)
        prefs[0]=1
        s=0
        count=0
        
        for i in nums:
            s+=i
            if(s-k) in prefs:
                count+=prefs[s-k]
            
            prefs[s]+=1
        return count
            
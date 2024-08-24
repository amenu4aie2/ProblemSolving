from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        data = {}

        for i in range(len(s)):


            if s[i] in data:
                if t[i] != data[s[i]]:
                    return False
            else:
                if t[i] in data.values():
                    return False
                data[s[i]] = t[i]
        
        return True
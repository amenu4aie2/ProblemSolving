import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p,x=re.subn(r'(\*)+','*',p)
        print(p)
        if(((re.fullmatch(p,s)))):
            # print(list(re.match(fr'^{p}$',s)))
            X=True
        else:
            # print(list(re.match(fr'^{p}$',s)))
            X=False
        return X
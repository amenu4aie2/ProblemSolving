class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        x=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                x.append(s[i:j])
        a=set(s)
        # print(x)
        max=0
        for i in x:
            flag=True
            for j in a:
                
                if(i.count(j)>2):
                    flag=False
            if(flag):
                if(len(i)>max):
                    max=len(i)
        return max
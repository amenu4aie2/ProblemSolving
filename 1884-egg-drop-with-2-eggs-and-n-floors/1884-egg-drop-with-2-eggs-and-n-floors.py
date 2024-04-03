
class Solution:
    def twoEggDrop(self, n: int) -> int:
        t=[[-1]*3 for i in range(1001)]
        def solve(e,f):
            if(f==0 or f==1):
                return f
            if(e==1):
                return f
            if(t[f][e]!=-1):
                return t[f][e]

            min_val=float('inf')
            for i in range(1,f+1):
                tmp= 1+ max(solve(e-1,i-1),solve(e,f-i))
                
                min_val=min(min_val,tmp)
                t[f][e]=min_val

            return min_val
        return solve(2,n)

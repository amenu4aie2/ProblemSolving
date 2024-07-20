
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        arr=[0]*(days[-1])
        for i in days:
            arr[i-1] = 1
        mc =float('inf')
        pd = [1,7,30]
        pdc = list(zip(pd,costs))
        d = set()
        def bt(i,c):
            d.add((i,c))
            nonlocal mc
            if i>=len(arr):
                mc = min(mc,c)
                return
            for j,k in pdc:
                
                if any(arr[i:i+j]): 
                    if (i+j,c+k) in d:
                        continue
                    bt(i+j,c+k)
                else:
                    if (i+j,c) in d:
                        continue
                    bt(i+j,c)
            return
        bt(0,0)
        return mc if mc!=float('inf') else -1
            
            
            
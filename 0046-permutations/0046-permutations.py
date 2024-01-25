class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def per(l,n):
            # print(f,l,n)
            if len(n)==1:
                l.append(n[0])
                print(l)
                f.append(l)
            
            for i in range(len(n)):
                t = l[:]
                print(t)
                t.append(n[i])
                per(t,n[:i]+n[i+1:])
        f= []
        per([],nums)
        return f
        

        
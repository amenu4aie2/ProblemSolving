class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a=[]
        x=[]
        out=[]

        for i in nums:


            if(len(a)==0):

                a.append(i)
            elif (len(a)==1):

                if(a[0]+1 ==i):

                    a.append(i)

                else:
                    out.append(a)

                    a=[i]
            else:


                if(a[1]+1 == i):
                    a[1]=i
                else:
                    out.append(a)
                    a=[i]
        if(len(a)>0):
            out.append(a)
        
            
        for i in out:
            if(len(i)>1 ):
                x.append(f"{i[0]}->{i[1]}")
                continue
            x.append(str(i[0]))
        return x
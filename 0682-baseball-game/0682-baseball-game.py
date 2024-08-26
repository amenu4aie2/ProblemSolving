class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr=[]
        for i in operations:
            if i=="D":
                if arr:
                    arr.append(arr[-1]*2)
            elif(i=="C"):
                if arr:
                    arr.pop()
            elif(i=="+"):
                a=[]
                for i in range(1,3):
                    if arr:
                        a.append(arr[-i])
                arr.append(sum(a))
            else:
                arr.append(int(i))
        return sum(arr)
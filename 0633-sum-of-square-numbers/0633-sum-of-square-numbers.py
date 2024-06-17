import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        tp=[]
        for i in range(int(math.sqrt(c))+1):
            tp.append(i**2)
        for i in tp:
            if (c-i) in tp:
                return True
        return False
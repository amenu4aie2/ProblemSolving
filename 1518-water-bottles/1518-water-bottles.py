class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank=0
        while numBottles>=numExchange:
            if(numBottles%numExchange==0):
                drank+=numBottles
                numBottles=numBottles/numExchange
            else:
                drank+=(numBottles//numExchange)*numExchange
                numBottles=(numBottles%numExchange)+(numBottles//numExchange)
        return int(drank+numBottles)
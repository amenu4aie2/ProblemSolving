class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        pointer=0
        time=0
        while(tickets[k]>0):
            if(tickets[pointer]>0):
                tickets[pointer]-=1
                
                time+=1
            pointer=(pointer+1)%len(tickets)            
            
            
        return time
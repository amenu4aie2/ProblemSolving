class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        x=list(preorder.split(','))
        balance=1
        for i in range(len(x)):
            try:
                if balance <= 0:
                    return False
                elif(int(x[i])):
                    balance+=1
                    
                

            
            except:
                balance-=1
            
        return balance==0
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            a=digits[i]+carry

            carry=a//10
            
            digits[i]=a%10
            
        x=[]
        if(carry>0):
            x.append(carry)
            
        x.extend(digits)
        return x

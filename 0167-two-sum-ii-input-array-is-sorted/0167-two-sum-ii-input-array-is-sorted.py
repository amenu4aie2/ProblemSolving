class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=[]
        size=1
        for i in range(len(numbers)):
            # if(target>=numbers[i]):
                if((target-numbers[i]) in numbers):
                    x.append(i+1)
                    x.append(size+numbers[i+1:].index(target-numbers[i])+1)
                    
                    break
                size+=1
        

        return x
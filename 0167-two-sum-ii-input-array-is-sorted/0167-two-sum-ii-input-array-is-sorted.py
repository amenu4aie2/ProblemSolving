class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=[]
        for i in range(len(numbers)):
            # if(target>=numbers[i]):
                if((target-numbers[i]) in numbers):
                    x.append(i+1)
                    x.append(len(numbers[:i+1])+numbers[i+1:].index(target-numbers[i])+1)
                    break
        

        return x
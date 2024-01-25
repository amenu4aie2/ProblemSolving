class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize pointers to the beginning and end of the array
        left = 0
        right = len(numbers) - 1
        
        # move the pointers inwards until the sum of the numbers at the pointers equals the target
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        
        # if no such pair of numbers exists, return an empty list
        return []
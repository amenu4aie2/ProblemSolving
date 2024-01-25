class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # combine the two arrays into one
        combined = nums1 + nums2
        
        # sort the combined array
        combined.sort()
        
        # calculate the median
        n = len(combined)
        if n % 2 == 0:
            # even number of elements, so take average of middle two
            return (combined[n//2 - 1] + combined[n//2]) / 2
        else:
            # odd number of elements, so middle element is median
            return combined[n//2]
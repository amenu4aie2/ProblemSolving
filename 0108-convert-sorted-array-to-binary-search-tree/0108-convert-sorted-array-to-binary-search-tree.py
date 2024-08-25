# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l,r=0,len(nums)-1
        root=TreeNode(nums[(l+r)//2])
        def recursion(l,r,x):
            
            if(l>r):
                return None
            
            x=TreeNode(nums[(l+r)//2])
            # print("hello world")
            x.left=recursion(l,((l+r)//2)-1,x.left)
            x.right=recursion(((l+r)//2)+1,r,x.right)
            return x
            

        root.left=recursion(l,((l+r)//2)-1,root.left)
        root.right=recursion(((l+r)//2)+1,r,root.right)
        return root
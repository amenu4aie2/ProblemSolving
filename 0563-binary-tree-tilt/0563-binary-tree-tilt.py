# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tilt=0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def recursion(root):
            if(root):
                x=recursion(root.left)
                y=recursion(root.right)
                self.tilt+=abs(x-y)
                return root.val+x+y
            else:
                return 0
        if(root):
            x=recursion(root.left)
            y=recursion(root.right)
            return self.tilt+abs(x-y)
        
        else:
            return self.tilt
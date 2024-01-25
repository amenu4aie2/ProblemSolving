# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = False
    def check(self, root, targetSum, s = 0):
        if root:
            s+=root.val
            if root.left==None and root.right==None and s==targetSum:
                self.out = True
                return
            if root.left==None and root.right==None and s!=targetSum:
                s=s-root.val
            
            
            self.check(root.left,targetSum,s)
            self.check(root.right,targetSum,s)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            if targetSum == 0 and root.left is None and root.right is None:
                return False
            self.check(root, targetSum)
            return self.out
        return False
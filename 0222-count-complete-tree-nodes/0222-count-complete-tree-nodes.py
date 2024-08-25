# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def recursion(root):
            if root:
                return recursion(root.left)+recursion(root.right)+1
            else:
                return 0

        return recursion(root)
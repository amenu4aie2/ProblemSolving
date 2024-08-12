# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head=root
        
        self.invertion(head)
        return head
    def invertion(self,root):
        if(root):
            if (root.right or root.left):
                root.right,root.left=root.left,root.right
                
                self.invertion(root.right)
                self.invertion(root.left)
            
        return 
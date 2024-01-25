# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkingheight(self,root):
        if root is None:
            return 0
        left=self.checkingheight(root.left)
        right=self.checkingheight(root.right)
        return max(left,right)+1
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        m=self.checkingheight(root)
        n=2**m-1
        res=[[""]*n for i in range(m)]
        low=0
        high=n
        def helper(root,rowCounter,low,high):
            if root is None:
                return None
            mid=(low+high)//2

            res[rowCounter][mid]=str(root.val)
            left=helper(root.left,rowCounter+1,low,mid-1)
            right=helper(root.right,rowCounter+1,mid+1,high)

        helper(root,0,low,high)
        return res
    
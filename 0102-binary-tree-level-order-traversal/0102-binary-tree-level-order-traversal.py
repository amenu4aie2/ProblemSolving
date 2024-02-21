# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()
        if not root:
            return []
        d.append([root])
        t = []
        v = 0
        while len(d)>0:
            a = d.popleft()
            n = []
            y = []
            for i in a:
                if i:
                    if i.left !=None:
                        n.append(i.left)
                    if i.right!=None:n.append(i.right)
                    y.append(i.val)
            if n:d.append(n)
            if y:t.append(y)
        print(t)
        return t
        

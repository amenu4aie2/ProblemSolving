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
        d.append([None])
        t = []
        v = 0
        while len(d)>1:
            a = d.popleft()
            n = []
            y = []
            # print(d)
            # print(len(d))
            for i in a:
                if i:
                    if i.left !=None:
                        n.append(i.left)
                    if i.right!=None:n.append(i.right)
                    y.append(i.val)
            if n:d.append(n)
            if y:t.append(y)
            if n:d.append([None])
        print(t)
        return t
        

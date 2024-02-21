# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def rec(root,q,i,array1,height=0):
            if(len(q)>0):
                a=q.popleft()
                if(a):
                    if(a.left):
                        q.append(a.left)
                        if(height==i):
                            array1.append(a.left.val)
                        array1=rec(a.left,q,i,array1,height+1)
                    if(a.right):
                        q.append(a.right)
                        if(height==i):
                            array1.append(a.right.val)
                        array1=rec(a.right,q,i,array1,height+1)
                    return array1
                    
                return array1
            
        def get_height(root,height):
            if root:
                height=max(get_height(root.right,height+1),get_height(root.left,height+1))
            
            return height

        h=get_height(root,0)
        print(h)
        b=None
        if(root):
            q=deque([root])
            # print(q)
            b=[[root.val]]
            for i in range(h+2):
                q=deque([root])
                array1=rec(root,q,i,[])
                # print(array1)
                if(array1):
                    b.append(array1.copy())
        return b
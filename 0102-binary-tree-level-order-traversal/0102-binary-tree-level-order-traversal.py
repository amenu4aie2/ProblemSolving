# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelo(q,array1,i,height=0):

            if(len(q)>0):

                a=q.popleft()
                
                if a:
                    
                    if(a.left):
                        if(height==i):
                            array1.append(a.left.val)
                        q.append(a.left)
                        array1=levelo(q,array1,i,height+1)
                        
                    if(a.right):
                        if(height==i):
                            array1.append(a.right.val)
                        q.append(a.right)
                        array1=levelo(q,array1,i,height+1)
                        
                    
                    return array1
                return array1
        def get_height(root,height=0):
            if root:
                if root.left is not None or root.right is not None:
                    return max(get_height(root.left,height+1),get_height(root.right,height+1))
                return height
            return height
        if(root):
            q=deque([root])
            h=get_height(root)
            b=[[root.val]]
            print(h)
            for i in range(h):
                q=deque([root])
                array1=levelo(q,[],i)
                if(len(array1)>0):
                    b.append(array1.copy())
            
            
            # 
            return b
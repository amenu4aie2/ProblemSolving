# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if  head==None or head.next == None:
            return head
        cur = head
    
        
        while cur and cur.next :
            if cur.val <= cur.next.val:
                cur=cur.next
            else:
                i = head
                pr = None
                while i.val <= cur.next.val:
                    pr = i
                    i = i.next
                if i == head :
                    head = cur.next
                    cur.next,head.next =cur.next.next,i
                    
                        
                else:
                    pr.next, cur.next.next,cur.next = cur.next, i,cur.next.next
                    
        return head
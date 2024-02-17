# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tmp=head
        
        while head and head.next:
            
            if((head.next.val==val) and (head.next.next)):
                head.next=head.next.next
                continue
            elif((head.next.val==val)):
                head.next=None
                continue
            head=head.next
        if(tmp):
            if(tmp.val==val and  tmp.next):
                tmp=tmp.next
            elif(tmp.val==val):
                return None

        return tmp
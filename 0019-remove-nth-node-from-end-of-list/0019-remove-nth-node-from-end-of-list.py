# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy=ListNode(0)
        dummy.next=head
        pointer=dummy
        curr=dummy
        for i in range(n):
            if(pointer):
                pointer=pointer.next
            else:
                return head
        
        
        while (pointer.next):
            curr=curr.next
            pointer=pointer.next
        
        curr.next=curr.next.next
        return dummy.next

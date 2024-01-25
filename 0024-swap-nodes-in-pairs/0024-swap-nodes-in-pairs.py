# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=None
    def swapPairs(self, l1: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while(l1):
            arr.append(l1.val)
            l1=l1.next
        i=0
        while i<(len(arr)-1):
            
            a=arr[i]
            b=arr[i+1]
            arr[i]=b
            arr[i+1]=a
            i+=2
        for i in arr:
            if self.head==None:
                l3=ListNode(i)
                self.head=l3
                continue
            l3.next=ListNode(i)
            l3=l3.next
        return self.head
            
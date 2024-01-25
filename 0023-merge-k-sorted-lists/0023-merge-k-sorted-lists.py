# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        # merge two sorted lists using a recursive divide-and-conquer approach
        def mergeTwoLists(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2
        
        # repeatedly merge pairs of lists until there is only one list left
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged = mergeTwoLists(l1, l2)
                merged_lists.append(merged)
            lists = merged_lists
        
        # return the final merged list (which is the only list left in the input)
        return lists[0]
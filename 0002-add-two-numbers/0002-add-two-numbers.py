# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def __init__(self):
        value=0
        self.value=value
        self.head=None
        self.l3=None
    def addTwoNumbers(self, l# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def __init__(self):
        value=0
        self.value=value
        self.head=None
        self.l3=None
    def addTwoNumbers(self, l1,l2,l3=None,value=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        # """
        
        if(l1 and l2):
            print(l1.val,l2.val)
            if(l3 is None):
                l3=ListNode((l1.val+l2.val+value)%10)
                self.head=l3
            else:
                # print(value)
                l3.next=ListNode((l1.val+l2.val+value)%10)
                l3=l3.next
            value=(l1.val+l2.val+value)/10
            return self.addTwoNumbers(l1.next,l2.next,l3,value)
        elif(l1):
            if(l3 is None):
                l3=ListNode((l1.val+value)%10)
                self.head=l3
            else:
                print(value)
                l3.next=ListNode((l1.val+value)%10)
                l3=l3.next
            value=(l1.val+value)//10
            
            return self.addTwoNumbers(l1.next,l2,l3,value)
        elif(l2):
            if(l3 is None):
                l3=ListNode((l2.val+value)%10)
                self.head=l3
            else:
                print(value)
                l3.next=ListNode((l2.val+value)%10)
                l3=l3.next
            value=(l2.val+value)//10
        
            return self.addTwoNumbers(l1,l2.next,l3,value)

        elif(value):
            l3.next=ListNode(value)
            l3=l3.next
            return self.addTwoNumbers(l1,l2,l3,0)
        else:
            
                
            return self.head
        1,l2,l3=None,value=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        # """
        
        if(l1 and l2):
            print(l1.val,l2.val)
            if(l3 is None):
                l3=ListNode((l1.val+l2.val+value)%10)
                self.head=l3
            else:
                # print(value)
                l3.next=ListNode((l1.val+l2.val+value)%10)
                l3=l3.next
            value=(l1.val+l2.val+value)/10
            return self.addTwoNumbers(l1.next,l2.next,l3,value)
        elif(l1):
            if(l3 is None):
                l3=ListNode((l1.val+value)%10)
                self.head=l3
            else:
                print(value)
                l3.next=ListNode((l1.val+value)%10)
                l3=l3.next
            value=(l1.val+value)//10
            
            return self.addTwoNumbers(l1.next,l2,l3,value)
        elif(l2):
            if(l3 is None):
                l3=ListNode((l2.val+value)%10)
                self.head=l3
            else:
                print(value)
                l3.next=ListNode((l2.val+value)%10)
                l3=l3.next
            value=(l2.val+value)//10
        
            return self.addTwoNumbers(l1,l2.next,l3,value)

        elif(value):
            l3.next=ListNode(value)
            l3=l3.next
            return self.addTwoNumbers(l1,l2,l3,0)
        else:
            
                
            return self.head
        

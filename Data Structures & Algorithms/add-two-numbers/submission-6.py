# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        ans = ListNode(0)
        copy = ans

        while curr1 and curr2:
            if curr1.val + curr2.val + ans.val > 9:
                ans.val += curr1.val + curr2.val - 10
                carry = 1
            else:
                carry = 0
                ans.val += curr1.val + curr2.val

            if carry == 1:
                ans.next = ListNode(1)
            else:
                if curr1.next or curr2.next:
                    ans.next = ListNode(0)
            
            curr1 = curr1.next
            curr2 = curr2.next
            ans = ans.next
        
        curr = curr1 or curr2

        while curr != None:
            if curr.val + ans.val > 9:
                ans.val += curr.val - 10
                ans.next = ListNode(1)
            else:
                ans.val += curr.val
                if curr.next:
                    ans.next = ListNode(0)
            
            curr = curr.next
            ans = ans.next
        
        return copy

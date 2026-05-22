# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        ans = curr

        num1 = l1
        num2 = l2

        while num1 and num2:
            if num1.val + num2.val + curr.val > 9:
                curr.val += num1.val + num2.val - 10
                curr.next = ListNode(1)
            else:
                curr.val += num1.val + num2.val
                if num1.next or num2.next:
                    curr.next = ListNode(0)
            
            curr = curr.next
            num1 = num1.next
            num2 = num2.next

        curr2 = num1 or num2

        while curr2 != None:
            if curr2.val + curr.val > 9:
                curr.val += curr2.val - 10
                curr.next = ListNode(1)
            else:
                curr.val += curr2.val
                if curr.next:
                    curr.next = ListNode(0)
            
            curr = curr.next
            curr2 = curr2.next

        return ans

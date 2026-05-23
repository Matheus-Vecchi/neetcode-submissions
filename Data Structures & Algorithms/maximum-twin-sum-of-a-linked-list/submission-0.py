# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None

        while curr != None:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        

        curr1 = head
        curr2 = prev

        ans = 0

        while curr2 != None:
            ans = max(ans, curr1.val + curr2.val)

            curr1 = curr1.next
            curr2 = curr2.next
        
        return ans
        

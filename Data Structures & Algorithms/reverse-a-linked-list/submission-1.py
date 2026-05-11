# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        curr = dummy
        prev = None

        while curr != None:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        
        return prev
        


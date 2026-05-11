# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            curr = head
        else:
            return False

        seen = []

        while curr.next and curr.next not in seen:
            seen.append(curr)
            curr = curr.next
        
        if curr.next and curr.next in seen:
            return True
        else:
            return False
        
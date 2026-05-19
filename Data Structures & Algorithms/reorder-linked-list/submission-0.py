# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr != None:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux

        curr = head

        while prev != None:
            aux = curr.next
            aux2 = prev.next

            curr.next = prev
            prev.next = aux

            curr = aux
            prev = aux2
        
        return 

            

        

        


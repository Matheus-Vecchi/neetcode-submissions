"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        count = 0
        hashmap = {}

        while curr != None:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        copy = hashmap[curr]

        ans = copy

        while curr != None:
            if curr.random:
                copy.random = hashmap[curr.random]
            if curr.next:
                copy.next = hashmap[curr.next]

            curr = curr.next
            if curr:
                copy = hashmap[curr]
            
        return ans


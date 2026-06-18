# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None

        def bst(root, k):
            nonlocal count, res
            if not root:
                return None
            
            bst(root.left, k)
            count += 1
            if count == k:
                res = root.val
                return
            bst(root.right, k)
        
        bst(root, k)
        return res
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            equal = True
            return equal
        
        if p and not q:
            equal = False
            return equal

        if not p and q:
            equal = False
            return equal
        
        if p.val != q.val:
            equal = False
            return equal
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
    
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def bst(root, k):
            if not root:
                return None
            
            bst(root.left, k)
            arr.append(root.val)
            bst(root.right, k)
        
        bst(root, k)
        return arr[k-1]

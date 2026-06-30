# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def dfs(root):
            nonlocal max_sum

            if not root:
                return 0
            
            left = max(dfs(root.left), 0) # -2
            right = max(dfs(root.right), 0) # 3

            max_sum = max(max_sum, root.val+left+right)
            
            return max(root.val + max(left, right), root.val)
        
        dfs(root)
        return max_sum
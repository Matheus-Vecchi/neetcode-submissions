# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_node = root.val
        ans = 0

        def dfs(root, max_node):
            nonlocal ans

            if not root:
                return
            
            if root.val >= max_node:
                ans += 1
                max_node = root.val
            
            dfs(root.left, max_node)
            dfs(root.right, max_node)
        
        dfs(root, max_node)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_node = root.val

        def dfs(root, max_node):
            if not root:
                return 0
            
            if root.val >= max_node:
                ans = 1
                max_node = root.val
            else:
                ans = 0
            
            left = dfs(root.left, max_node)
            right = dfs(root.right, max_node)

            return ans + left + right

        return(dfs(root, max_node))
        
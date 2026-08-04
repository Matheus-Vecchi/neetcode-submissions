# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(preorder, inorder):
            if not inorder or not preorder:
                return

            root = TreeNode(preorder[0])
            val = inorder.index(root.val)

            
            root.left = dfs(preorder[1:], inorder[:val])
            root.right = dfs(preorder[len(inorder[:val+1]):], inorder[val+1:])

            
            return root

        return dfs(preorder, inorder)
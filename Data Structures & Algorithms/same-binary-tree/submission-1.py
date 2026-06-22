# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_ans = []
        q_ans = []

        def p_dfs(p):
            if not p:
                p_ans.append(None)
                return None

            p_ans.append(p.val)            
            left = p_dfs(p.left)
            right = p_dfs(p.right)

            return None
        
        def q_dfs(q):
            if not q:
                q_ans.append(None)
                return None
            
            q_ans.append(q.val)
            left = q_dfs(q.left) # []
            right = q_dfs(q.right) # 7

            return None
        
        p_dfs(p)
        q_dfs(q)

        return p_ans == q_ans

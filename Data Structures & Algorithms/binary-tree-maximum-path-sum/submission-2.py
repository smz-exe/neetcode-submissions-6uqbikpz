# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # calculate global res, return len of max oneway path
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            len_left = max(0, dfs(node.left))
            len_right = max(0, dfs(node.right))

            res[0] = max(res[0], len_left + len_right + node.val)

            return node.val + max(len_left, len_right)
        
        dfs(root)
        
        return res[0]
        
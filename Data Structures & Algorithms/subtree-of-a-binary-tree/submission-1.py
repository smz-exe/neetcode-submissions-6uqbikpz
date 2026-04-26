# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p, q):
            if (not p and not q) or (p and q and p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)):
                return True
            else:
                return False
        
        def dfs(head, subRoot):
            if not head:
                return False
            
            if isSame(head, subRoot):
                return True
            return dfs(head.left, subRoot) or dfs(head.right, subRoot)
        
        return dfs(root, subRoot)

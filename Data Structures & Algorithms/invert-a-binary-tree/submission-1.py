# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def invert(node: TreeNode):
            if not node.left and not node.right:
                return 
            else:
                left = node.left
                node.left = node.right
                node.right = left

                if node.left:
                    invert(node.left)
                if node.right:
                    invert(node.right)
            
        invert(root)
        return root

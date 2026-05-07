# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# pattern: binary tree, preorder traversal, DFS
# data structure: binary tree
# time complexity: O(n)


class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                preorder.append("N")
                return None
            
            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))

        def dfs() -> TreeNode | None:
            val = next(vals)
            if val == "N":
                return None
            
            root = TreeNode(val)
            root.left = dfs()
            root.right = dfs()
            
            return root
        
        return dfs()





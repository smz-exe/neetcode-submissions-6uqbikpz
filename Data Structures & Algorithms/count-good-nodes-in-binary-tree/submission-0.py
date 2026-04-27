# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        q.append((root, root.val)) # (node, prevMax)

        while q:
            qLen = len(q)

            for i in range(qLen):
                node, prevMax = q.popleft()
                if node:
                    val = node.val
                    if val >= prevMax:
                        res += 1
                        prevMax = val

                    q.append((node.left, prevMax))
                    q.append((node.right, prevMax))
        
        return res
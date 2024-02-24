# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(big, root):
            if not root: return 0
            isGood = 0
            if root.val >= big:
                isGood = 1
                big = root.val
            return isGood + dfs(big, root.left) + dfs(big, root.right)
        return dfs(-10000, root)

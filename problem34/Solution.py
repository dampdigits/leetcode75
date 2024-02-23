# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leftLeaves, rightLeaves = [], []
        def dfs(root, branch):
            if root.left: dfs(root.left, branch)
            if root.right: dfs(root.right, branch)
            # add root to leaves if no child
            elif not root.left:
                if branch == 'r':
                    rightLeaves.append(root.val)
                else: leftLeaves.append(root.val)          
            
        dfs(root1, 'l')
        dfs(root2, 'r')
        return leftLeaves == rightLeaves

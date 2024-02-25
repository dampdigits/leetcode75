# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def zigzag_dfs(root, dir):
            if not root: return 0
            nonlocal longest
            curr_longest = 1

            left = zigzag_dfs(root.left, 'l')
            right = zigzag_dfs(root.right, 'r')

            if dir == 'l': curr_longest += right
            else: curr_longest += left
            
            longest = max(longest, curr_longest)
            return curr_longest

        zigzag_dfs(root.left, 'l')
        zigzag_dfs(root.right, 'r')
        return longest

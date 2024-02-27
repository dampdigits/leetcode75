# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, curr_level, max_level, queue = root.val, 0, 1, [root]

        while queue:
            curr_level += 1
            n, curr_sum = len(queue), 0

            # Remove nodes of this level & add nodes of the next level
            for i in range(n):
                front = queue.pop(0)
                curr_sum += front.val
                if front.left: queue.append(front.left)
                if front.right: queue.append(front.right)
            
            # Update max_level if sum of current level is greater
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = curr_level
        
        return max_level

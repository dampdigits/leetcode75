# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    stack = []  # list to store nodes in dfs
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Return 0 if node == None
        if not root: return 0

        # Add current node to stack
        self.stack.append(root.val)
        paths, curr_sum = 0, sum(self.stack)

        ''' Think of sum as a queue
            Find targetSums in current queue '''
        for i in range(len(self.stack)):
            if curr_sum == targetSum: paths += 1
            # Remove front element from sum
            curr_sum -= self.stack[i]
        
        # Find targetSums in left & right branches using dfs
        leftPaths = self.pathSum(root.left, targetSum)
        rightPaths = self.pathSum(root.right, targetSum)

        # Remove current node from stack and return
        self.stack.pop()
        return paths + leftPaths + rightPaths

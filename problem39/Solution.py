# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Return empty list if root is null
        if not root: return []

        # DFS left & right branches and store theirs lists
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)

        # Remember sizes of left & right lists
        l = 0 if not left else len(left)
        r = 0 if not right else len(right)

        # If right list is longer, return root and right list
        if r >= l:
            return [root.val] + right

        ''' Otherwise return root + right list +
            the part of left list that is longer '''
        return [root.val] + right + left[r:]

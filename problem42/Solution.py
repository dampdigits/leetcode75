# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Previous root, current root and direction
        prev, curr, dir = None, root, 0

        # dfs till key is found
        while curr:
            # Search left if current root > key
            if curr.val > key:
                prev = curr
                curr = curr.left
                dir = 0 # 0 means left
            
            # Search right if current root < key
            elif curr.val < key:
                prev = curr
                curr = curr.right
                dir = 1 # 0 means right
            
            else: # If current root == key
                node = curr.right

                if not node: # If no right subtree
                    if not prev:
                        root = curr.left
                        break
                    if dir: prev.right = curr.left
                    else: prev.left = curr.left
                    break
                
                # Find left-most node in right subtree of key
                while node.left: node = node.left

                # Append left subtree of key to left of node
                node.left = curr.left
                if not prev:
                    root = curr.right
                    break
                
                # Remove key
                if dir: prev.right = curr.right
                else: prev.left = curr.right
                break
        return root

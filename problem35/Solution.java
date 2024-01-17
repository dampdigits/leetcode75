/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + goodLeaves(root.val, root.left) + goodLeaves(root.val, root.right);
    }
    private int goodLeaves(int max, TreeNode root) {
        if (root == null)
            return 0;
        if (root.val >= max)
            return 1 + goodLeaves(root.val, root.left) + goodLeaves(root.val, root.right);
        else
            return 0 + goodLeaves(max, root.left) + goodLeaves(max, root.right);
    }
}

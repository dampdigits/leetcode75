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
    int ans = 0;
    public int longestZigZag(TreeNode root) {
        zigzag(root.left, -1);
        zigzag(root.right, 1);
        return ans;
    }
    private int zigzag(TreeNode root, int branch) {
        if (root == null)
            return 0;
        int tmp = 1;
        int left = zigzag(root.left, -1);
        int right = zigzag(root.right, 1);
        if (branch == -1)
            tmp += right;
        else
            tmp += left;
        ans = Math.max(ans, tmp);
        return tmp;
    }
}

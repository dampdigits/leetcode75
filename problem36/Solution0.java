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
    int counter = 0;
    public int pathSum(TreeNode root, int sum) {

        if (root == null) return 0;

        pathSumHelper(root, sum);
        pathSum(root.left, sum);
        pathSum(root.right, sum);

        return counter;
    }

    void pathSumHelper(TreeNode root, long currentSum) {
        if (root == null) return;
        
        if (currentSum == root.val)
            counter++;
        
        pathSumHelper(root.left, currentSum - root.val);
        pathSumHelper(root.right, currentSum - root.val);
    } 
}

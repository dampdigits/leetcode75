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
    int count = 0;
    List<Integer> path = new ArrayList<>();
    public int pathSum(TreeNode root, int sum) {
        pathSumHelper(root, sum);
        return count;
    }

    void pathSumHelper(TreeNode root, long sum) {
        if (root == null) return;
        
        path.add(root.val);

        pathSumHelper(root.left, sum);
        pathSumHelper(root.right, sum);

        long tmpSum = 0;
        for (int i = path.size()-1; i >= 0; i--) {
            tmpSum += path.get(i);
            if (sum == tmpSum)
                count++;
        }
        path.remove(path.size()-1);
    } 
}

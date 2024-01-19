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
    public int maxLevelSum(TreeNode root) {
        List<Integer> levelSums = new ArrayList<>();
        levelSums = levelSumList(root);
        int i = 0, maxLevel = 0;
        while (i < levelSums.size()) {
            if (levelSums.get(i) > levelSums.get(maxLevel))
                maxLevel = i;
            i++;
        }
        return maxLevel+1;
    }
    private List<Integer> levelSumList(TreeNode root) {
        if (root == null)
            return new ArrayList<>();

        List<Integer> left = new ArrayList<>();
        left = levelSumList(root.left);

        List<Integer> right = new ArrayList<>();
        right = levelSumList(root.right);

        List<Integer> level = new ArrayList<>();
        level.add(root.val);

        int len = Math.min(left.size(), right.size());
        for (int i = 0; i < len; i++)
            level.add(left.get(i) + right.get(i));

        if (left.size() < right.size())
            level.addAll(level.size(), right.subList(left.size(), right.size()));

        else if (left.size() > right.size())
            level.addAll(level.size(), left.subList(right.size(), left.size()));
        
        return level;
    }
}

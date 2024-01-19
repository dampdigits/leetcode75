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
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null)
            return new ArrayList<>();
        List<Integer> leftBranch = new ArrayList<>();
        leftBranch = rightSideView(root.left);

        List<Integer> rightBranch = new ArrayList<>();
        rightBranch = rightSideView(root.right);

        List<Integer> finalBranch = new ArrayList<>();
        finalBranch.add(root.val);
        
        if (rightBranch.size() < leftBranch.size()) {
            finalBranch.addAll(rightBranch);
			// finalBranch.addAll(finalBranch.size(), leftBranch.subList(rightBranch.size(), leftBranch.size()));
			// or
            for (int i = rightBranch.size(); i < leftBranch.size(); i++) {
                finalBranch.add(leftBranch.get(i));
            }
        } else
            finalBranch.addAll(rightBranch);
        return finalBranch;
    }
}

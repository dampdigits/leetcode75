import java.util.Arrays;
class Solution {
    public static void main(String[] args) {
		int nums[] = {3,1,3,4,3}, k = 6;
		System.out.println(maxOperations(nums, k));
    }
	public static int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int l = 0;
        int h = nums.length - 1;
        int ans = 0;
        while (l < h) {
            int sum = nums[l] + nums[h];
            if (sum == k) {
                ans++;
                l++;
                h--;
            } else if (sum < k) {
                l++;
            } else {
                h--;
            }
        }
        return ans;
    }
}

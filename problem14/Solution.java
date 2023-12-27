public class Solution {
	public static void main(String[] args) {
		int nums[] = {1,12,-5,-6,50,3}, k = 4;
		System.out.println(findMaxAverage(nums, k));
	}
	public static double findMaxAverage(int[] nums, int k) {
		int max = 0;
		for (int i = 0; i < k; i++)
			max += nums[i];
        int curr = max;
		for (int i = k; i < nums.length; i++) {
			curr = curr - nums[i - k] + nums[i];
			max = Math.max(curr, max);
		}
		return (double) max / k;
    }
}

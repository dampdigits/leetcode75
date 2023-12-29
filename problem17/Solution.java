class Solution {
    public static int longestSubarray(int[] nums) {
        int prev = 0, curr = 0, max = 0;
		for (int num : nums) {
			if (num == 1)
				++curr;
			else {
				max = Math.max(max, prev + curr);
				prev = curr;
				curr = 0;
			}
		}
		max = Math.max(max, prev + curr);
		return max == nums.length ? max - 1 : max;
    }
	public static void main(String[] args) {
		int nums[] = {1,1,1};
		System.out.println(longestSubarray(nums));
	}
}

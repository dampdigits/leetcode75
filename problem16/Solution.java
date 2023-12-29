class Solution {
    public static int longestOnes(int[] nums, int k) {
		int start = 0, end = 0, zeroes = 0;
		for (end = 0; end < nums.length; end++) {
			if (nums[end] == 0)
				++zeroes;
			if (zeroes > k) {
				if (nums[start] == 0)
					--zeroes;
				++start;
			}
		}
		return end - start;
	}
	public static void main(String[] args) {
		int nums[] = {0,0,1,1,1,0,0}, k = 0;
		System.out.println(longestOnes(nums, k));
	}
}

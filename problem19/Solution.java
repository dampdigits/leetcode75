class Solution {
    public static int pivotIndex(int[] nums) {
        int second = 0, first = 0;
		for (int num : nums)
			second += num;
		for (int i = 0; i < nums.length; i++) {
			second -= nums[i];
			if (first == second)
				return i;
			first += nums[i];
		}
		return -1;
    }
	public static void main(String[] args) {
		int nums[] = {2,1,-1};
		System.out.println(pivotIndex(nums));
	}
}

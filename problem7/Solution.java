class Solution {
    public int[] productExceptSelf(int[] nums) {
        int ans[] = new int[nums.length];
		int zeroes = 0;
		int idx = -1;
		double product = 1;
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] == 0) {
				if (zeroes == 1)
					return ans;
				idx = i;
				++zeroes;
			}
			else
				product *= nums[i];
		}
		if (idx != -1) {
			ans[idx] = (int) product;
			return ans;
		}
		for (int i = 0; i < nums.length; i++) {
			ans[i] = (int)(product * Math.pow(nums[i], -1));
		}
		return ans;
    }
}

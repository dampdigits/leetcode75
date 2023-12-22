public class Solution {
	public static void main(String[] args) {
		int nums[] = {1,8,0,5,5,0,0,2,10};
		moveZeroes(nums);
		for (int num : nums) {
			System.out.println(num);
		}
}
    public static void moveZeroes(int[] nums) {
       int zeroes = 0, len = nums.length;
	   for (int i = 0; i < len; i++)
			if (nums[i] == 0)
				++zeroes;
			else
				if (zeroes != 0)
					nums[i - zeroes] = nums[i];

	   for (int i = len - 1; i >= len - zeroes; i--)
		   nums[i] = 0;
	}
}

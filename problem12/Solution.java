class Solution {
	public static void main(String[] args) {
		int arr[] = {1,8,6,2,5,4,8,3,7};
		System.out.println(maxArea(arr));
	}
    public static int maxArea(int[] height) {
		int max = 0, left = 0, right = height.length - 1;
        while (left < right) {
			int h = Math.min(height[left], height[right]);
			max = Math.max(max, h * (right - left));
			while (height[left] <= h && left < right)
				++left;
			while (height[right] <= h && left < right)
				--right;
        }
		return max;
    }
}

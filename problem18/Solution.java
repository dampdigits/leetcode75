class Solution {
    public static int largestAltitude(int[] gain) {
        int highest = 0, sum = 0;
		for (int i : gain) {
			sum += i;
			highest = Math.max(highest, sum);
		}
		return highest;
    }
	public static void main(String[] args) {
		int gain[] = {-4,-3,-2,-1,4,3,2};
		System.out.println(largestAltitude(gain));
	}
}

public class Solution {
	public static void main(String[] args) {
		int arr[] = {1,2,40,5,6,-80};
		System.out.println(increasingTriplet(arr));
	}

	public static boolean increasingTriplet(int[] nums) {
	  int max1 = Integer.MAX_VALUE;
	   int max2 = Integer.MAX_VALUE;
	   for(int n : nums) {
		   if(n <= max1)
				max1 = n;
		   else if(n <= max2)
			   max2 = n;
		   else
			   return true;
	   }
	   return false;
	}
}

import java.util.*;

class Solution {
    public static List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
		List<List<Integer>> answer = new ArrayList<>();
        Set<Integer> set1 = new HashSet<>(), set2 = new HashSet<>();

        for (int num : nums1)
            set1.add(num);

        for (int num : nums2)
            if (!set1.contains(num))
                set2.add(num);

        for (int num : nums2)
			if (set1.contains(num))
                set1.remove(num);

        answer.add(new ArrayList<>(set1));
        answer.add(new ArrayList<>(set2));
		return answer;
    }
	public static void main(String[] args) {
		int nums1[] = {-3,6,-5,4,5,5};
		int nums2[] = {6,6,-3,-3,3,5};
		System.out.println(findDifference(nums1, nums2));
	}
}

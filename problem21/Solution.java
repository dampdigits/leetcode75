import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Map;

class Solution {
    public static boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
		for (int i : arr)
			map.put(i, map.getOrDefault(i, 0) + 1);
		Set<Integer> set = new HashSet<>(map.values());
		return map.size() == set.size();
    }
	public static void main(String[] args) {
		int arr[] = {1,2,2,1,1,3};
		System.out.println(uniqueOccurrences(arr));
	}
}

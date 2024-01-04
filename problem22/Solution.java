import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public static boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length())
			return false;
		
		Map<Character, Integer> charCount1 = new HashMap<>();
		Map<Character, Integer> charCount2 = new HashMap<>();
		Set<Character> chars1 = new HashSet<>();
		Set<Character> chars2 = new HashSet<>();
        Map<Integer, Integer> countFreq1 = new HashMap<>();
        Map<Integer, Integer> countFreq2 = new HashMap<>();

		char arr1[] = word1.toCharArray();
		char arr2[] = word2.toCharArray();

		for (int i = 0; i < arr2.length; i++) {
			chars1.add(arr1[i]);
			chars2.add(arr2[i]);
			charCount1.put(arr1[i], charCount1.getOrDefault(arr1[i],0) + 1);
			charCount2.put(arr2[i], charCount2.getOrDefault(arr2[i],0) + 1);
		}

		if (chars1.size() != chars2.size())
			return false;

		for (Character ch : chars2)
			if (! chars1.contains(ch))
				return false;

		for (Integer value : charCount1.values()) {
			if (! charCount2.containsValue(value))
				return false;
            countFreq1.put(value, countFreq1.getOrDefault(value, 0) + 1);
        }

        for (Integer value : charCount2.values()) {
			if (! charCount1.containsValue(value))
				return false;
            countFreq2.put(value, countFreq2.getOrDefault(value, 0) + 1);
        }

        for (Integer key : countFreq1.keySet())
            if (countFreq1.get(key) != countFreq2.get(key))
                return false;

		return true;
    }
	public static void main(String[] args) {
		String word1 = "a", word2 = "aa";
		System.out.println(closeStrings(word1, word2));
	}
}

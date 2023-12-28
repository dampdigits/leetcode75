class Solution {
    public static int maxVowels(String s, int k) {
        int curr = 0;
		char vowels[] = {'a', 'e', 'i', 'o', 'u'};
		char ch[] = s.toCharArray();
		for (int i = 0; i < k; i++)
			for (char vowel : vowels)
				if (vowel == ch[i]) {
					++curr;
				break;
				}
		int max = curr;
		for (int i = k; i < ch.length; i++) {
			int found = 0;
			for (char vowel : vowels) {
				if (vowel == ch[i]) {
					++curr;
					++found;
				}
				if (vowel == ch[i - k]) {
					--curr;
					++found;
				}
				if (found == 2)
					break;
			}
			max = Math.max(max, curr);
		}
		return max;
    }

	public static void main(String[] args) {
		String s = "leetcode";
		int k = 3;
		System.out.println(maxVowels(s, k));
	}
}

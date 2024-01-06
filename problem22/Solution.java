import java.util.Arrays;

class Solution {
    public static boolean closeStrings(String word1, String word2) {
        if(word1.length()!=word2.length())
			return false;
        
		int w1[]=new int[26];
        int w2[]=new int[26];
        
		for(char ch:word1.toCharArray())
            w1[ch-'a']++;

        for(char ch:word2.toCharArray()){
            if(w1[ch-'a']==0) return false;
            w2[ch-'a']++;
        }

        Arrays.sort(w1);
        Arrays.sort(w2);
        return Arrays.equals(w1,w2);
    }
	public static void main(String[] args) {
		String word1 = "cabbba", word2 = "caabbb";
		System.out.println(closeStrings(word1, word2));
	}
}

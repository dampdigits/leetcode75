class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();
        int shorter = Math.min(word1.length(), word2.length());
        
        for (int i = 0; i < shorter; i++) {
            merged.append(word1.charAt(i)).append(word2.charAt(i));
        }
        
        if (word1.length() > word2.length()) {
            merged.append(word1, shorter, word1.length());
        } else if (word1.length() < word2.length()) {
            merged.append(word2, shorter, word2.length());
        }
        
        return merged.toString();
    }
}

class Solution {
    public String reverseWords(String s) {
        // Split the input string using space (" ") as the delimiter
        String[] words = s.split(" ");

        // Use StringBuilder for more efficient string concatenation
        StringBuilder reversed = new StringBuilder();

        // Iterate through the words in reverse order
        for (int i = words.length - 1; i >= 0; i--) {
            String word = words[i].trim(); // Trim each word to remove leading and trailing spaces

            // Check if the word is not empty before appending
            if (!word.isEmpty()) {
                reversed.append(word).append(" ");
            }
        }

        // Trim the trailing space and convert StringBuilder to String
        return reversed.toString().trim();
    }
}

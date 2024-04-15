class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort words in ascending order
        products.sort()
        suggestions = []  # Final list of suggestions

        # Pointers for the range of words that contain the prefix
        start, end = 0, len(products)-1

        for i in range(len(searchWord)):
            c = searchWord[i]
            curr_suggestions = []

            while (start <= end) and (len(products[start]) <= i or products[start][i] != c):
                start += 1
            
            while (start <= end) and (len(products[end]) <= i or products[end][i] != c):
                end -= 1
            
            # Count of words containing prefix
            wordCount = end - start +1

            # Add at most 3 words to the list of current suggestions
            for j in range(min(3, wordCount)):
                curr_suggestions.append(products[start + j])
            
            # Add current suggestions list to the final list of suggestions
            suggestions.append(curr_suggestions)

        return suggestions

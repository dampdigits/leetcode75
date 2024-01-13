class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for char1, char2 in zip(word1, word2):
            result += char1 + char2
        start = len(word1) if len(word1) < len(word2) else len(word2)
        result += word1[start:] + word2[start:]

        return result

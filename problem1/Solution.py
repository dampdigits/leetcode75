class Solution:
    def mergeAlternatively(self, word1: str, word2: str) -> str:
        result = ""
        for char1, char2 in zip(word1, word2):
            result += char1 + char2

        result += word1[len(result):] + word2[len(result):]

        return result

    def main(self):
        # Use self.mergeAlternatively instead of mergeAlternatively
        print(self.mergeAlternatively("abc", "pqr"))

if __name__ == "__main__":
    solution = Solution()
    solution.main()


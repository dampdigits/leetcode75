class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text2), len(text1)
        cache = [[0] * (m +1) for _ in range(n +1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]: cache[i][j] = cache[i+1][j+1] +1
                else: cache[i][j] = max(cache[i+1][j], cache[i][j+1])
        
        return cache[0][0]

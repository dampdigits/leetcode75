class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        cache = [[0] * m for _ in range(n)]
        has_cache = [[False] * m for _ in range(n)]

        def findLCS(i, j):
            if i == n or j == m: return 0
            if has_cache[i][j]: return cache[i][j]

            if text1[i] != text2[j]:
                cache[i][j] = max(
                    findLCS(i+1, j),
                    findLCS(i, j+1)
                )
            else: cache[i][j] = findLCS(i+1, j+1) +1
            
            has_cache[i][j] = True
            return cache[i][j]

        return findLCS(0,0)

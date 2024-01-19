class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        slen, tlen = len(s), len(t)
        while i < slen and j < tlen:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == slen


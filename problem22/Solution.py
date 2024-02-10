class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        for c1, c2 in zip(word1, word2):
            freq1[ord(c1) - 97] += 1
            freq2[ord(c2) - 97] += 1
        
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False
        freq1.sort()
        freq2.sort()
        return freq1 == freq2
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        letters = []
        ans, count, i = 0, 0, 0
        for c in s:
            if i == k:
                i -= 1
                if letters.pop(0):
                    count -= 1
            if c in 'aeiou':
                letters.append(True)
                count += 1
            else:
                letters.append(False)
            ans = max(ans, count)
            i += 1
        return ans

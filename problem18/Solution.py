class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = height = 0
        for g in gain:
            height += g
            maxHeight = max(maxHeight, height)
        return maxHeight

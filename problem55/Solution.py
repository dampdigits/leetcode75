class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums_ = sorted(enumerate(nums), key=lambda x:x[1])
        return nums_[-1][0]

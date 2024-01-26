class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = end = len(nums) - 1
        zeros = 0
        while end >= 0:
            if nums[end] == 0:
                zeros += 1
            end -= 1
            if zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start -= 1
        return start - end - 1

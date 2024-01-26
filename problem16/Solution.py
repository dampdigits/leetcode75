class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = len(nums)-1
        zeros = 0
        while end >= 0:
            if nums[end] == 0:
                zeros += 1
            end -= 1
            if zeros > k:
                if nums[start] == 0:
                    zeros -= 1
                start -= 1
        return start - end


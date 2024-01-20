class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = sum(nums[len(nums)-k:])
        print(f"maxAvg = {maxAvg}")
        l, r = len(nums)-k, len(nums) - 1
        tmp = maxAvg
        while l > 0:
            l -= 1
            tmp = tmp + nums[l] - nums[r]
            r -= 1
            maxAvg = max(maxAvg, tmp)
        print(maxAvg)
        return maxAvg / k

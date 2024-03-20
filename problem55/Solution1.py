class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n-1
        while i < j:
            mid = i + ((j - i)>>1)
            if mid > 0 and nums[mid] < nums[mid-1]: j = mid-1
            elif mid < n-1 and nums[mid] < nums[mid+1]: i = mid+1
            else: return mid
        return i

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = rightSum = 0
        for num in nums: # Calculate rightSum
            rightSum += num

        for i in range(len(nums)): # Calculate leftSum
            rightSum -= nums[i] # Reduce rightSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

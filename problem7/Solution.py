class Solution:
    def productExceptSelf(self, nums):
        size = len(nums)
        result = [1]*size

        left, right = 1, 1

        for i in range(size):
            reverse_i = size-1-i
            result[i] *= left
            result[reverse_i] *= right

            left *= nums[i]
            right *= nums[reverse_i]

        return result

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        smallest = smaller = max(nums)

        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= smaller:
                smaller = num
            else:
                return True                
        return False

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -1 * heapq.heappop(nums)

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs, heap, minNum2, maxVal, tmpSum = [], [], 100000, 0, 0
        # Create max heap of pairs sorted using nums2
        for i, num in enumerate(nums2):
            heapq.heappush(pairs, (-num, nums1[i]))
        
        i = 0
        while pairs:
            # Create min heap of nums1 of k elements
            num2, num1 = heapq.heappop(pairs)
            tmpSum += num1
            heapq.heappush(heap, num1)
            minNum2 = min(minNum2, -num2)
            i += 1
            # Multiply and compare after heap of k nums1 elements have been created
            if i >= k:
                maxVal = max(maxVal, minNum2 * tmpSum)
                tmpSum -= heapq.heappop(heap)
        return maxVal

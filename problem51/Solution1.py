class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x:x[1], reverse=True)
        n1_sum = score = heapSize = 0
        minHeap = []
        heapify(minHeap)

        for n1, n2 in pairs:
            n1_sum += n1
            heappush(minHeap, n1)
            heapSize += 1

            if heapSize > k:
                n1 = heappop(minHeap)
                n1_sum -= n1
                heapSize -= 1
            if heapSize == k: score = max(score, n1_sum*n2)

        return score

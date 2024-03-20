class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        if len(piles) == h: return ans
        l, r = 1, ans
        piles.sort(reverse=True)

        while l <= r:
            mid = l + ((r-l)>>1)
            hrs = 0

            for pile in piles:
                hrs += ceil(pile / mid)
                if hrs > h: break
            
            if hrs > h:
                l = mid+1
            else:
                ans = mid
                r = mid-1

        return ans

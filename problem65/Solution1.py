class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # For memoization
        cache = [[-1] * 2 for _ in range(len(prices))]

        def findProfit(i, canBuy):
            if i == len(prices): return 0
            if cache[i][canBuy] != -1: return cache[i][canBuy]
            profit = 0

            if canBuy:
                # Choose max between buy & dont buy today
                profit = max(
                    -prices[i] + findProfit(i+1, 0),
                    findProfit(i+1, 1)
                )
            else:
                # Choose max between sell & sell another day
                profit = max(
                    prices[i] + findProfit(i+1, 1) - fee,
                    findProfit(i+1, 0)
                )
            
            # Memoization
            cache[i][canBuy] = profit
            return profit
        
        return findProfit(0, 1)

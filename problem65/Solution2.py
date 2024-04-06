class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_price = prices[0] + fee
        max_profit = 0

        for price in prices:
            if min_price < price:
                # Sell stock at this price
                max_profit += price - min_price
                
                min_price = price

            elif price + fee < min_price:
                # Buy stock at this price
                min_price = price+fee
        
        return max_profit

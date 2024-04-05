class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        has_buy_cache = [False] * days
        buy_cache = [None] * days

        def buy(day):
            if day == days: return 0
            if has_buy_cache[day]: return buy_cache[day]

            # Buy stock this day & sell another day
            profit = sell(day+1) - prices[day]

            # Buy stock another day
            profit = max(profit, buy(day+1))

            buy_cache[day] = profit
            has_buy_cache[day] = True
            return profit

        has_sell_cache = [False] * days
        sell_cache = [None] * days

        def sell(day):
            if day == days: return 0
            if has_sell_cache[day]: return sell_cache[day]
            
            # Sell stock this day & buy another day
            profit = prices[day] + buy(day+1) - fee

            # Sell stock another day
            profit = max(profit, sell(day+1))

            sell_cache[day] = profit
            has_sell_cache[day] = True
            return profit

        return buy(0)

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        while self.stack and self.stack[-1]['price'] <= price:
            span += self.stack.pop()['span']

        self.stack.append({'price': price, 'span': span})
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

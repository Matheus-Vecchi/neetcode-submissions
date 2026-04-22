class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        self.stack.append(price)
        count = -1
        span = 0
        while abs(count) <= len(self.stack) and price >= self.stack[count]:
            count -= 1
            span += 1
        
        return span
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
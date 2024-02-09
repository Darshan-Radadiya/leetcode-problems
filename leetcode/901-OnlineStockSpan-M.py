class StockSpanner:

    def __init__(self):
        self.stack = [] # it will be tuple of price and span

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        return span

obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))
print("Expected output is[1,1,1,2,1,4,6]")
print("Time Complexity is O(n)")
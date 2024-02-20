class RecentCounter:
    def __init__(self):
        self.queue = []
        self.counter = 0
    
    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.counter += 1

        while self.queue[0] < t-3000:
            self.queue.pop(0)
            self.counter -= 1
        
        return self.counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

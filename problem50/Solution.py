class SmallestInfiniteSet:

    def __init__(self):
        self.inf_set = []
        self.curr = 1

    def popSmallest(self) -> int:
        if self.inf_set:
            return heapq.heappop(self.inf_set)
        self.curr += 1
        return self.curr - 1

    def addBack(self, num: int) -> None:
        if num >= self.curr or num <= 0: return
        if num not in self.inf_set:
            heapq.heappush(self.inf_set, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

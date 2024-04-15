class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        removed = 0
        prev_end = intervals[0][0]

        for start, end in intervals:
            if prev_end <= start: prev_end = end
            else: removed += 1

        return removed

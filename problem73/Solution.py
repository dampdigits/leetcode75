class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        shots, x = 0, points[0][1]

        for start, end in points:
            if x < start:
                shots += 1
                x = end
            elif x > end: x = end
        
        return shots + 1

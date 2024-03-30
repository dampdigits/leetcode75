class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memoization
        pathCache = [[0] * n for _ in range(m)]

        def move(i,j):
            if i == m-1 and j == n-1: return 1
            if pathCache[i][j]: return pathCache[i][j]

            paths = 0
            
            # Go down if row < m-1
            if i < m-1: paths += move(i+1, j)

            # Go up if column < n-1
            if j < n-1: paths += move(i, j+1)

            pathCache[i][j] = paths
            return paths

        return move(0,0)

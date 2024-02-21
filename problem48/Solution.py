class Solution:
    def orangesRotting(self, grid):
        good_oranges, bad_oranges = 0, 0
        rottenList = [] # list to remember coordinates of rotten oranges
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: good_oranges += 1
                elif grid[i][j] == 2:
                    bad_oranges += 1
                    rottenList.append([i,j])
        
        if good_oranges == 0: return 0
        if bad_oranges == 0: return -1
        
        mins = 0
        dirs = [[-1,0], [1,0], [0,-1], [0,1]] # 4 directions

        # 1 iteration = 1 minute
        while True:
            rot = 0
            new_rot = []
            # rot adjacent fresh oranges
            for rotten in rottenList:
                i, j = rotten[0], rotten[1]
                for dir in dirs:
                    new_i, new_j = i+dir[0], j+dir[1]
                    # check new coordinates are within boundaries
                    if new_i >= 0 and new_i < m and new_j >=0 and new_j < n and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        good_oranges -= 1
                        bad_oranges =+ 1
                        new_rot.append([new_i, new_j])
                        rot += 1
            if rot == 0: break
            rottenList = new_rot
            mins += 1
        return (mins if good_oranges == 0 else -1)

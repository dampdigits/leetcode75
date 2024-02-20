class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue, steps = [], 0
        m, n = len(maze), len(maze[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        queue.append(entrance)
        maze[entrance[0]][entrance[1]] = '+'    # create wall to mark visited

        # bfs
        while (queue):
            N = len(queue)
            while N:
                coordinates = queue.pop(0)
                i, j = coordinates[0], coordinates[1]
                # exit found if at a boundary which is not the entrance
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and coordinates != entrance:
                    return steps
                # explore 4 directions
                for dir in directions:
                    # create new coordinates
                    new_i = i + dir[0]
                    new_j = j + dir[1]
                    # check new coordinates are within boundary and there is no wall
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and maze[new_i][new_j] == '.':
                        queue.append([new_i, new_j])
                        maze[new_i][new_j] = '+'    # create wall to mark visited
                N -= 1
            steps += 1
        return -1

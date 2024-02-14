def equalPairs(grid):
    count = 0
    cols = []
    n = len(grid)
    for i in range(n):
        col = []
        for j in range(n):
            col.append(grid[j][i])
        cols.append(col)
    for row in grid:
        for col in cols:
            if col == row:
                count += 1
    return count

def main():
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    print("equal row and column pairs: ", equalPairs(grid))

if __name__ == "__main__":
    main()

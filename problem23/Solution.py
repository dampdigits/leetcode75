def equalPairs(grid):
    count = 0   # to store number of equal rows & columns
    cols = []    # List to store columns
    n = len(grid)
    
    # Add columns to to cols
    for i in range(n):
        col = [] # Empty list to store a column
        for j in range(n):
            col.append(grid[j][i])
        cols.append(col)

    # Find equal rows and columns
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

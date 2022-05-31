def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
        if row < 0 or col < 0 or row == rows or col == cols or grid[row][
                col] != '1':
            return

        grid[row][col] = '2'

        dfs(row + 1, col)
        dfs(row, col + 1)
        dfs(row - 1, col)
        dfs(row, col - 1)

    islands = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                dfs(row, col)
                islands += 1

    return islands

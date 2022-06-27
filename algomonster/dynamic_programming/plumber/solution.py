def plumber(grid):
    for row in grid:
        row.append(-1)

    prev_row = []
    start = 0
    coins = 0
    for i, val in enumerate(grid[0]):
        if val == 0:
            pass
        elif val == 1:
            coins += 1
        elif val == -1:
            for _ in range(start, i):
                prev_row.append(coins)
            prev_row.append(float('-inf'))
            start = i + 1
            coins = 0

    for level in range(1, len(grid)):
        cur_row = []
        row = grid[level]
        prev_max = float('-inf')
        start = 0
        coins = 0

        for i, val in enumerate(row):
            if val == 0:
                prev_max = max(prev_max, prev_row[i])
            elif val == 1:
                prev_max = max(prev_max, prev_row[i])
                coins += 1
            elif val == -1:
                for _ in range(start, i):
                    cur_row.append(prev_max + coins)
                cur_row.append(float('-inf'))
                start = i + 1
                coins = 0
                prev_max = float('-inf')

        prev_row = cur_row

    cur_max = max(cur_row)
    if cur_max < 0:
        return -1
    return cur_max
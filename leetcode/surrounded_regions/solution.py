def solve(board):
    rows = len(board)
    cols = len(board[0])

    def dfs(row, col):
        if row < 0 or col < 0 or row == rows or col == cols or board[row][
                col] != 'O':
            return

        board[row][col] = 'T'

        dfs(row + 1, col)
        dfs(row, col + 1)
        dfs(row - 1, col)
        dfs(row, col - 1)

    # 1. Run dfs on all border cells
    for row in len(rows):
        for col in len(rows):
            if board[row][col] == 'O' and (row in [0, rows - 1]
                                           or col in [0, cols - 1]):
                dfs(row, col)

    # 2. Swap T with O and O with X
    for row in len(rows):
        for col in len(rows):
            if board[row][col] == 'T':
                board[row][col] = 'O'
            elif board[row][col] == 'O':
                board[row][col] = 'X'

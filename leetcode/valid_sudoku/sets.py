def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for row in range(9):
        for col in range(9):
            val = board[row][col]
            if val == '.':
                continue
            if val in rows[row]:
                return False
            else:
                rows[row].add(val)
            if val in cols[col]:
                return False
            else:
                cols[col].add(val)
            box = row // 3 * 3 + col // 3
            if val in boxes[box]:
                return False
            else:
                boxes[box].add(val)
    return True

from collections import deque

delta_row = [1, 0, -1, 0]
delta_col = [0, 1, 0, -1]
target = ((1, 2, 3), (4, 5, 0))


def num_steps(init_pos):
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0

    moves_map = {init_pos: 0}
    moves_queue = deque([init_pos])
    while len(moves_queue) > 0:
        move = moves_queue.popleft()

        row, col = 0, 0
        for i in range(len(move)):
            for j in range(len(move[i])):
                if move[i][j] == 0:
                    row, col = i, j

        for i in range(len(delta_row)):
            new_row = row + delta_row[i]
            new_col = col + delta_col[i]
            if 0 <= new_row < 2 and 0 <= new_col < 3:
                new_state = list(list(line) for line in move)
                new_state[new_row][new_col], new_state[row][col] = new_state[
                    row][col], new_state[new_row][new_col]
                new_move = tuple(tuple(line) for line in new_state)

                if new_move not in moves_map:
                    moves_map[new_move] = moves_map[move] + 1
                    moves_queue.append(new_move)
                    if new_move == target:
                        return moves_map[new_move]

    return -1

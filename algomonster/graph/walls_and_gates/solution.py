from collections import deque


def map_gate_distances(dungeon_map):
    INF = 2147483647
    delta_row = [0, 1, 0, -1]
    delta_col = [1, 0, -1, 0]
    num_rows = len(dungeon_map)
    num_cols = len(dungeon_map[0])

    queue = deque()
    for i in range(num_rows):
        for j in range(num_cols):
            if dungeon_map[i][j] == 0:
                queue.append((i, j))

    while len(queue) > 0:
        row, col = queue.popleft()
        for i in range(len(delta_row)):
            move_row = row + delta_row[i]
            move_col = col + delta_col[i]
            if 0 <= move_row < num_rows and 0 <= move_col < num_cols:
                if dungeon_map[move_row][move_col] == INF:
                    dungeon_map[move_row][move_col] = dungeon_map[row][col] + 1
                    queue.append((move_row, move_col))

    return dungeon_map
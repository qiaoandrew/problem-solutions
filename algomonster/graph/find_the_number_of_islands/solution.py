from collections import deque


def count_number_of_islands(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbours(node):
        neighbours = []
        row, col = node

        delta_row = [1, 0, -1, 0]
        delta_col = [0, 1, 0, -1]

        for i in range(len(delta_row)):
            neighbour_row = row + delta_row[i]
            neighbour_col = col + delta_col[i]

            if 0 <= neighbour_row < num_rows and 0 <= neighbour_col < num_cols:
                neighbours.append((neighbour_row, neighbour_col))

        return neighbours

    def bfs(start):
        queue = deque([start])

        row, col = start
        grid[row][col] = 2

        while len(queue) > 0:
            node = queue.popleft()
            neighbours = get_neighbours(node)
            for neighbour in neighbours:
                row, col = neighbour
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    queue.append(neighbour)

    count = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                bfs((row, col))
                count += 1
    return count
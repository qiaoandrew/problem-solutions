from collections import deque


def flood_fill(r, c, replacement, image):

    num_rows, num_cols = len(image), len(image[0])

    def get_neighbours(node, color):
        row, col = node
        delta_col = [0, 1, 0, -1]
        delta_row = [1, 0, -1, 0]
        for i in range(len(delta_col)):
            neighbour_col = col + delta_col[i]
            neighbour_row = row + delta_row[i]
            if 0 <= neighbour_col < num_cols and 0 <= neighbour_row < num_rows:
                if image[neighbour_row][neighbour_col] == color:
                    yield neighbour_row, neighbour_col

    def bfs(root):
        queue = deque([root])
        visited = [[False for col in range(num_cols)]
                   for row in range(num_rows)]

        row, col = root
        color = image[row][col]
        image[row][col] = replacement
        visited[row][col] = True

        while len(queue) > 0:
            cur_node = queue.popleft()
            for neighbour in get_neighbours(cur_node, color):
                row, col = neighbour
                if visited[row][col] == True:
                    continue
                image[row][col] = replacement
                queue.append(neighbour)
                visited[row][col] = True

    bfs((r, c))
    return image
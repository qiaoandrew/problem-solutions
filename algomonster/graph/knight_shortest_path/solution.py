from collections import deque


def get_knight_shortest_path(x, y):

    def get_moves(coord):
        x, y = coord
        moves = []
        delta_x = [1, 2, 2, 1, -1, -2, -2, -1]
        delta_y = [2, 1, -1, -2, -2, -1, 1, 2]

        for i in range(len(delta_x)):
            move_x = x + delta_x[i]
            move_y = y + delta_y[i]
            moves.append((move_x, move_y))

        return moves

    def bfs(start):
        queue = deque([start])
        visited = set([start])
        steps = 0

        while len(queue) > 0:
            num_moves = len(queue)

            for _ in range(num_moves):
                coord = queue.popleft()
                if coord[0] == x and coord[1] == y:
                    return steps

                for move in get_moves(coord):
                    if move in visited:
                        continue

                    queue.append(move)
                    visited.add(move)

            steps += 1

    return bfs((0, 0))
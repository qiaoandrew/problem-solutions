from collections import deque


def shorted_path(graph, a, b):

    def get_neighbours(node):
        return graph[node]

    def dfs(root, target):
        queue = deque([root])
        visited = set([root])

        distance = 0
        while len(queue) > 0:
            num_neighbours = len(queue)
            for _ in range(num_neighbours):
                cur_node = queue.popleft()
                if cur_node == target:
                    return distance

                for neighbour in get_neighbours(cur_node):
                    if neighbour in visited:
                        continue
                    queue.append(neighbour)
                    visited.add(neighbour)

            distance += 1

    return dfs(a, b)

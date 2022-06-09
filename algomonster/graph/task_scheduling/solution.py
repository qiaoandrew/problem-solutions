from collections import deque


def task_scheduling(tasks, requirements):

    # Returns a hash table with how many tasks point to a task
    def count_parents(graph):
        counts = {node: 0 for node in graph}
        for parent in graph:
            for node in graph[parent]:
                counts[node] += 1
        return counts

    def topological_sort(graph):
        res = []
        queue = deque()
        counts = count_parents(graph)

        for node in counts:
            if counts[node] == 0:
                queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()
            res.append(node)
            for child in graph[node]:
                counts[child] -= 1
                if counts[child] == 0:
                    queue.append(child)

        return res if len(graph) == len(res) else None

    graph = {t: [] for t in tasks}
    for a, b in requirements:
        graph[a].append(b)
    return topological_sort(graph)

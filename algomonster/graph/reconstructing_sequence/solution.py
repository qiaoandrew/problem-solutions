from collections import deque


def sequence_reconstruction(original, seqs):

    def count_parents(graph):
        num_parents = {node: 0 for node in graph}
        for parent in graph:
            for child in graph[parent]:
                num_parents[child] += 1
        return num_parents

    def topological_sort(graph):
        seq = []
        queue = deque()

        num_parents = count_parents(graph)
        for node in num_parents:
            if num_parents[node] == 0:
                queue.append(node)

        while len(queue) > 0:
            if len(queue) > 1:
                return False

            node = queue.popleft()
            seq.append(node)

            for child in graph[node]:
                num_parents[child] -= 1
                if num_parents[child] == 0:
                    queue.append(child)

        return seq == original

    graph = {node: set() for node in range(1, 1 + len(original))}
    for seq in seqs:
        for i in range(len(seq) - 1):
            source, destination = seq[i], seq[i + 1]
            graph[source].add(destination)
    return topological_sort(graph)

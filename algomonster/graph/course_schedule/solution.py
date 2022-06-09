from collections import deque


def is_valid_course_schedule(n, prerequisites):

    def get_dependencies(graph):
        dependencies = {dependent: 0 for dependent in graph}
        for dependency in graph:
            for dependent in graph[dependency]:
                dependencies[dependent] += 1
        return dependencies

    def topological_sort(graph):
        res = []
        queue = deque()
        dependencies = get_dependencies(graph)

        for dependent in dependencies:
            if dependencies[dependent] == 0:
                queue.append(dependent)

        while len(queue) > 0:
            dependency = queue.popleft()
            res.append(dependency)
            for dependent in graph[dependency]:
                dependencies[dependent] -= 1
                if dependencies[dependent] == 0:
                    queue.append(dependent)

        return True if len(graph) == len(res) else False

    # Create a graph using
    graph = {course: [] for course in range(n)}
    for dependent, dependency in prerequisites:
        graph[dependent].append(dependency)
    return topological_sort(graph)

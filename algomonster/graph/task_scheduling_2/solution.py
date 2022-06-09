from collections import deque


def task_scheduling_2(tasks, times, requirements):

    def count_dependencies(graph):
        num_dependencies = {dependent: 0 for dependent in graph}
        for dependency in graph:
            for dependent in graph[dependency]:
                num_dependencies[dependent] += 1
        return num_dependencies

    def topological_sort(graph, task_times):
        ans = 0
        queue = deque()
        # Time from start to end of a node
        total_time = {dependent: 0 for dependent in graph}
        # Map of node to its dependencies
        num_dependencies = count_dependencies(graph)

        # Determine which tasks can be done at the beginning
        for dependent in num_dependencies:
            if num_dependencies[dependent] == 0:
                queue.append(dependent)
                total_time[dependent] = task_times[dependent]
                ans = max(ans, total_time[dependent])

        while len(queue) > 0:
            dependency = queue.popleft()
            for dependent in graph[dependency]:
                num_dependencies[dependent] -= 1
                total_time[dependent] = max(
                    total_time[dependent],
                    total_time[dependency] + task_times[dependent])
                ans = max(ans, total_time[dependent])
                if num_dependencies[dependent] == 0:
                    queue.append(dependent)

        return ans

    # Dictionary to map each node to the nodes that dependent on them
    graph = {task: [] for task in tasks}
    # Dictionary to map task to time it takes
    task_times = {tasks[i]: times[i] for i in range(len(tasks))}
    for dependency, dependent in requirements:
        graph[dependency].append(dependent)

    return topological_sort(graph, task_times)

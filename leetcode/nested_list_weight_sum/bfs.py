from collections import deque


def depth_sum(nested_list):
    queue = deque(nested_list)
    depth = 1
    total = 0
    while queue:
        level_length = len(queue)
        for _ in range(level_length):
            nested = queue.popleft()
            if nested.isInteger():
                total += nested.getInteger() * depth
            else:
                queue.extendright(nested.getList())
        depth += 1
    return total
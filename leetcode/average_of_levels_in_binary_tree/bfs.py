from collections import deque


def average_of_levels(root):
    averages = []
    queue = deque([root])
    while queue:
        level_sum = 0
        level_length = len(queue)
        for _ in range(level_length):
            cur_node = queue.popleft()
            level_sum += cur_node.val
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        averages.append(level_sum / level_length)
    return averages

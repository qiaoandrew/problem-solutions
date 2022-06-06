from collections import deque


def level_order_traversal(root):
    levels = []
    queue = deque([root])
    while len(queue) > 0:
        level_length = len(queue)
        cur_level = []
        for _ in range(level_length):
            cur_node = queue.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        levels.append(cur_level)
    return levels

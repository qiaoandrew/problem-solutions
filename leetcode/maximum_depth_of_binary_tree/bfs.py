from collections import deque


def max_depth(root):
    if not root:
        return 0
    levels = 0
    queue = deque([root])
    while queue:
        levels += 1
        level_length = len(queue)
        for _ in range(level_length):
            cur_node = queue.popleft()
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    return levels

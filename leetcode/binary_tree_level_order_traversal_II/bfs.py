from collections import deque


def level_order_bottom(root):
    levels = deque()
    if not root:
        return levels
    queue = deque([root])
    while queue:
        level_length = len(queue)
        cur_level = []
        for _ in range(level_length):
            cur_node = queue.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        levels.appendleft(cur_level)
    return levels

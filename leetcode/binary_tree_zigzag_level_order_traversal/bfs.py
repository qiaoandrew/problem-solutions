from collections import deque


def zigzap_level_order(root):
    levels = []
    if not root:
        return levels
    queue = deque([root])
    left_to_right = True
    while queue:
        cur_level = deque()
        level_length = len(queue)
        for _ in range(level_length):
            cur_node = queue.popleft()
            if left_to_right:
                cur_level.append(cur_node.val)
            else:
                cur_level.appendleft(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        levels.append(list(cur_level))
        left_to_right = not left_to_right
    return levels

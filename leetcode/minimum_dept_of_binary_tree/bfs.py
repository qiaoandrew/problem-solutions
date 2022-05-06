from collections import deque


def min_depth(root):
    if root is None:
        return 0
    levels = 0
    queue = deque([root])
    while queue:
        levels += 1
        level_length = len(queue)
        for _ in range(level_length):
            cur_node = queue.popleft()
            if not cur_node.left and not cur_node.right:
                return levels
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

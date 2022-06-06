from collections import deque


def binary_tree_min_depth(root):
    queue = deque([root])
    cur_level = 0

    while len(queue) > 0:
        level_length = len(queue)

        for _ in range(level_length):
            cur_node = queue.popleft()

            if cur_node.left is None and cur_node.right is None:
                return cur_level

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        cur_level += 1
    return cur_level

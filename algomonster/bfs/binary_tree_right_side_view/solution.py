from collections import deque


def binary_tree_right_side_view(root):
    right_side = []
    queue = deque([root])
    while len(queue) > 0:
        level_length = len(queue)
        right_side.append(queue[0])
        for _ in range(level_length):
            cur_node = queue.popleft()
            if cur_node.right:
                queue.append(cur_node.right)
            if cur_node.left:
                queue.append(cur_node.left)
    return right_side

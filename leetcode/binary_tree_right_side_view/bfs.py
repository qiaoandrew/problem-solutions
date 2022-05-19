from collections import deque


def right_side_view(root):
    if root is None:
        return root
    queue = deque([root])
    result = []
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            cur_node = queue.popleft()
            if i == level_length - 1:
                result.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    return result

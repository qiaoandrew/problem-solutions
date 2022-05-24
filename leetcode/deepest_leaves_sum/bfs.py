from collections import deque


def deepest_leaves_sum(root):
    queue = deque([root])
    while queue:
        level_length = len(queue)
        cur_level_sum = 0
        for _ in range(level_length):
            cur_node = queue.popleft()
            cur_level_sum += cur_node.val
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        if not queue:
            return cur_level_sum

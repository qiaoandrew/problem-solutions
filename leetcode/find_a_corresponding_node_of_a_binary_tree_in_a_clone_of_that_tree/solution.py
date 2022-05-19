from collections import deque


def get_target_copy(original, cloned, target):
    queue = deque([cloned])
    while queue:
        cur_node = queue.popleft()
        if cur_node.val == target.val:
            return cur_node
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return None


def get_target_copy_better(original, cloned, target):
    queue_original = deque([original])
    queue_cloned = deque([cloned])

    while queue_original:
        node_original = queue_original.popleft()
        node_cloned = queue_cloned.popleft()
        if node_original is target:
            return node_cloned

        if node_original.left:
            queue_cloned.append(node_cloned.left)
            queue_original.append(node_original.left)
        if node_original.right:
            queue_cloned.append(node_cloned.right)
            queue_original.append(node_original.right)

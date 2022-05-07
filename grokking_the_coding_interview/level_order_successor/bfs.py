from collections import deque


def find_successor(root, key):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        cur_node = queue.popleft()
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
        if cur_node.val == key:
            break
    return queue[0] if queue else None

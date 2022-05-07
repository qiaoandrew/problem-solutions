from collections import deque


def invert_tree(root):
    if not root:
        return None

    queue = deque([root])
    while queue:
        cur_node = queue.popleft()
        cur_node.left, cur_node.right = cur_node.right, cur_node.left
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return root

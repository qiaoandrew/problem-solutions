from collections import deque


def connect(root):
    if not root:
        return root
    queue = deque([root])
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            cur_node = queue.popleft()
            if i < level_length - 1:
                cur_node.next = queue[0]
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    return root
from collections import deque


def is_symmetric(root):
    queue = deque([root, root])
    while queue:
        n1 = queue.popleft()
        n2 = queue.popleft()
        if n1 is None and n2 is None:
            continue
        elif n1 is None or n2 is None:
            return False
        elif n1.val != n2.val:
            return False
        queue.append(n1.left)
        queue.append(n2.right)
        queue.append(n1.right)
        queue.append(n2.left)
    return True

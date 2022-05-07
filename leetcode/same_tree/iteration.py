from collections import deque


def is_same_tree(p, q):

    def check(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True

    queue = deque([(p, q)])
    while queue:
        p, q = deque.popleft()
        if not check(p, q):
            return False
        if p:
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
    return True

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p.val is None or q.val is None:
        return False
    is_same_tree(p.left, q.left)
    is_same_tree(p.right, q.right)

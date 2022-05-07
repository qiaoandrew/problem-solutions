def has_path_sum(root, target_sum):
    if not root:
        return False
    stack = [(root, target_sum - root.val)]
    while stack:
        node, cur_sum = stack.pop()
        if not node.left and not node.right and cur_sum == 0:
            return True
        if node.right:
            stack.append((node.right, cur_sum - node.right.val))
        if node.left:
            stack.append((node.left, cur_sum - node.left.val))
    return False

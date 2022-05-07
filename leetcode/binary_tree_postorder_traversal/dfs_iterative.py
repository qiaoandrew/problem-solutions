def postorder_traversal(root):
    if root is None:
        return []
    traverse_list = []
    stack = [root]
    while stack:
        cur_node = stack.pop()
        if cur_node is not None:
            traverse_list.append(cur_node.val)
            stack.append(cur_node.left)
            stack.append(cur_node.right)
    return traverse_list[::-1]

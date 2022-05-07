def preorder_traversal(root):
    if root is None:
        return []
    traverse_list = []
    stack = [root]
    while stack:
        cur_node = stack.pop()
        if cur_node is not None:
            traverse_list.append(cur_node.val)
            if cur_node.right is not None:
                stack.append(cur_node.right)
            if cur_node.left is not None:
                stack.append(cur_node.left)
    return traverse_list

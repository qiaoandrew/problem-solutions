def inorder_traversal(root):
    traverse_list = []
    stack = []
    cur_node = root
    while cur_node or stack:
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
        cur_node = stack.pop()
        traverse_list.append(cur_node.val)
        cur_node = cur_node.right
    return traverse_list

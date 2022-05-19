def inorder_successor(root, p):
    successor = None
    cur_node = root
    while cur_node:
        if p.val >= cur_node.val:
            cur_node = cur_node.right
        else:
            successor = cur_node
            cur_node = cur_node.left
    return successor

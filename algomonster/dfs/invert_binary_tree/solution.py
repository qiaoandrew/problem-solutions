def invert_binary_tree(root):
    if root:
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)
        root.right, root.left = root.left, root.right
    return root
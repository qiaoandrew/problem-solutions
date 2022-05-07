def invert_tree(root):
    if root:
        invert_tree(root.left)
        invert_tree(root.right)
        root.right, root.left = root.left, root.right
    return root

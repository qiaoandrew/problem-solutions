def recover_tree(root):
    x = y = prev = None

    def dfs(node):
        nonlocal x, y, prev
        if node is None:
            return

        dfs(node.left)
        if prev and node.val < prev.val:
            y = node
            if x is None:
                x = prev
            else:
                return
        prev = node
        dfs(node.right)

    dfs(root)
    x.val, y.val = y.val, x.val
def is_valid_bst(root):

    def dfs(node, min_val, max_val):
        if root is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return dfs(root.left, min_val, root.val) and dfs(
            root.right, root.val, max_val)

    return dfs(root, -float('inf'), float('inf'))

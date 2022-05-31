def tree_max_depth(root):

    def dfs(root):
        if root is None:
            return 0

        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root)

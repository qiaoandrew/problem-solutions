def lca(root, p, q):
    ans = None

    def dfs(node):
        nonlocal ans
        if node is None:
            return False

        left = dfs(node.left)
        right = dfs(node.right)

        mid = node == p or node == q

        if mid + left + right >= 2:
            ans = node

        return mid or left or right

    dfs(root)
    return ans

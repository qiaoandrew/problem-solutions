def flatten(root):

    def dfs(node):
        if node is None:
            return None

        if node.left is None and node.right is None:
            return node

        left_tail = dfs(node.left)
        right_tail = dfs(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        if right_tail:
            return right_tail
        else:
            return left_tail

    dfs(root)

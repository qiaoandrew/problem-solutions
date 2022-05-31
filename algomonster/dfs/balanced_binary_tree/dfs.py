def is_balanced(tree):

    def tree_height(node):
        if node is None:
            return 0

        left_height = tree_height(node.left)
        right_height = tree_height(node.right)

        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) >= 2:
            return -1

        return max(left_height, right_height) + 1

    return tree_height(tree) != -1

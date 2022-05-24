def diameter_of_binary_tree(root):
    diameter = 0

    def longest_path(cur_node):
        if not cur_node:
            return 0

        nonlocal diameter
        left_path = longest_path(cur_node.left)
        right_path = longest_path(cur_node.right)
        diameter = max(diameter, left_path + right_path)

        return max(left_path, right_path) + 1

    longest_path(root)
    return diameter
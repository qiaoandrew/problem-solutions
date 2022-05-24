def max_path_sum(root):
    max_sum = -float('inf')

    def find_sum(cur_node):
        if not cur_node:
            return 0

        nonlocal max_sum

        left_sum = max(find_sum(cur_node.left), 0)
        right_sum = max(find_sum(cur_node.right), 0)

        path_sum = left_sum + right_sum + cur_node.val
        max_sum = max(max_sum, path_sum)

        return cur_node.val + max(left_sum, right_sum)

    find_sum(root)
    return max_sum

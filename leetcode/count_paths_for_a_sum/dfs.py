def path_sum(root, target_sum):
    return find_paths(root, target_sum, [])


def find_paths(cur_node, cur_target, cur_path):
    if cur_node is None:
        return 0

    cur_path.append(cur_node.val)
    path_count, path_sum = 0, 0
    for i in range(len(cur_path) - 1, -1, -1):
        path_sum += cur_path[i]
        if path_sum == cur_target:
            path_count += 1

    path_count += find_paths(cur_node.left, path_sum, cur_path)
    path_count += find_paths(cur_node.right, path_sum, cur_path)

    del cur_path[-1]

    return path_count
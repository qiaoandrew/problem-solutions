def path_sum(root, target_sum):
    paths = []
    find_paths(root, target_sum, [], paths)
    return paths


def find_paths(cur_node, target_sum, cur_path, paths):
    if not cur_node:
        return
    cur_path.append(cur_node.val)
    if cur_node.val == target_sum and not cur_node.left and not cur_node.right:
        paths.append(list(cur_path))
    else:
        find_paths(cur_node.left, target_sum - cur_node.val, cur_path, paths)
        find_paths(cur_node.right, target_sum - cur_node.val, cur_path, paths)
    del cur_path[-1]
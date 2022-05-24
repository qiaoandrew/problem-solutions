def isValidSequence(root, arr):
    return check_valid_sequence(root, arr, 0)


def check_valid_sequence(cur_node, arr, level):
    if cur_node is None:
        return False

    if level >= len(arr) or cur_node.val != arr[level]:
        return False

    if cur_node.left is None and cur_node.right is None and cur_node.val == arr[
            level] and level == len(arr) - 1:
        return True

    return check_valid_sequence(cur_node.left, arr,
                                level + 1) or check_valid_sequence(
                                    cur_node.right, arr, level + 1)

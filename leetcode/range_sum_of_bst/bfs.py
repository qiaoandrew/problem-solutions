from collections import deque


def range_sum_bst(root, low, high):
    if root is None:
        return 0

    sum = 0
    queue = deque([root])
    while queue:
        cur_node = queue.popleft()
        if cur_node.val >= low and cur_node.val <= high:
            sum += cur_node.val
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return sum

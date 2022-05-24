from collections import deque


def sum_even_grandparent(root):
    total_sum = 0
    queue = deque([root])

    while queue:
        cur_node = queue.popleft()
        if cur_node.left is not None:
            queue.append(cur_node.left)
            if cur_node.val % 2 == 0:
                if cur_node.left.left is not None:
                    total_sum += cur_node.left.left.val
                if cur_node.left.right is not None:
                    total_sum += cur_node.left.right.val
        if cur_node.right is not None:
            queue.append(cur_node.right)
            if cur_node.val % 2 == 0:
                if cur_node.right.right is not None:
                    total_sum += cur_node.right.right.val
                if cur_node.right.left is not None:
                    total_sum += cur_node.right.left.val

    return total_sum
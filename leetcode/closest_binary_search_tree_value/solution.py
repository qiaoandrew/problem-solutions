def closest_value(root, target):
    closest = float('inf')

    next_node = root
    while next_node:
        if abs(next_node.val - target) < abs(closest - target):
            closest = next_node.val

        if next_node.val > target:
            next_node = next_node.left
        else:
            next_node = next_node.right

    return closest

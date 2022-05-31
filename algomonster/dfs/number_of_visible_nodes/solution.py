def visible_tree_node(root):

    def find_visible_nodes(node, cur_max):

        if node is None:
            return 0

        total = 0
        if node.val >= cur_max:
            total += 1
            cur_max = node.val

        total += find_visible_nodes(node.left, cur_max)
        total += find_visible_nodes(node.right, cur_max)

        return total

    return find_visible_nodes(root, -float('inf'))

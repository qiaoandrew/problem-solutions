def copy_random_list(head):

    def helper(head):
        if not head:
            return None

        if head in visited_nodes:
            return visited_nodes[head]

        node = Node(head.val, None, None)
        visited_nodes[head] = node

        node.next = helper(head.next)
        node.random = helper(head.random)

        return node

    visited_nodes = {}
    return helper(head)

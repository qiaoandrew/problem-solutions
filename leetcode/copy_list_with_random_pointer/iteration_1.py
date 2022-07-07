def copy_random_list(head):
    visited = {}

    def get_cloned_node(node):
        if node:
            if node in visited:
                return visited[node]
            else:
                visited[node] = Node(node.val, None, None)
                return visited[node]
        return None

    if not head:
        return head

    old_node = head
    new_node = Node(old_node.val, None, None)
    visited[old_node] = new_node

    while old_node:
        new_node.random = get_cloned_node(old_node.random)
        new_node.next = get_cloned_node(old_node.next)

        old_node = old_node.next
        new_node = new_node.next

    return visited[head]

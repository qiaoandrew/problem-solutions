def insert(head, insert_val):
    if not head:
        new_node = Node(insert_val, None)
        new_node.next = new_node
        return new_node

    prev, cur = head, head.next
    to_insert = False

    while True:
        if prev.val <= insert_val <= cur.val:
            to_insert = True
        elif prev.val > cur.val:
            if insert_val >= prev.val or insert_val <= cur.val:
                to_insert = True

        if to_insert:
            prev.next = Node(insert_val, cur)
            return head

        prev, cur = cur, cur.next
        if prev == head:
            break

    prev.next = Node(insert_val, cur)
    return head
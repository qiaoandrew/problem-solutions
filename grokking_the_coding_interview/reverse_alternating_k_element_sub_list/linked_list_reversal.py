def reverse_k_group(head, k):
    if k == 1 and head is None:
        return head

    cur, prev = head, None
    while cur is not None:
        last_node_prev_part = prev
        last_node_cur_list = cur

        i = 0
        while cur is not None and i < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            i += 1

        if last_node_prev_part is not None:
            last_node_prev_part.next = prev
        else:
            head = prev
        last_node_cur_list.next = cur

        i = 0
        while cur is not None and i < k:
            prev = cur
            cur = cur.next
            i += 1
    return head
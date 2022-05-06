def reverse_between(head, left, right):
    if left >= right:
        return head
    cur = head
    prev = None
    i = 0
    while cur is not None and i < left - 1:
        prev = cur
        cur = cur.next
        i += 1
    last_node_first_part = prev
    last_node_sub_list = cur
    next_temp = None
    i = 0
    while cur is not None and i < right - left + 1:
        next_temp = cur.next
        cur.next = prev
        prev = cur
        cur = next_temp
        i += 1
    if last_node_first_part is not None:
        last_node_first_part.next = prev
    else:
        head = prev
    last_node_sub_list.next = cur
    return head

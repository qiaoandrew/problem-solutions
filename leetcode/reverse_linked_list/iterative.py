def reverse_list(head):
    prev = None
    cur = head
    while cur:
        temp_next = cur.next
        cur.next = prev
        prev = cur
        cur = temp_next
    return prev

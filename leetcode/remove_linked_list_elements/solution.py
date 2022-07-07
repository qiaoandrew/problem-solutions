def remove_elements(head, val):
    sentinel = ListNode(0)
    sentinel.next = head

    prev, cur = sentinel, head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return sentinel.next

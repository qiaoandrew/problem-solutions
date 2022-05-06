def reverse_list(head):
    if not head or not head.next:
        return head
    p = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p
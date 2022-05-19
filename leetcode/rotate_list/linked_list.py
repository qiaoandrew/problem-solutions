def rotate_right(head, k):
    if head is None or head.next is None:
        return head

    length = 1
    last = head
    while last.next is not None:
        last = last.next
        length += 1

    last.next = head
    rotations = k % length
    new_head_distance_from_current_head = length - rotations

    new_tail = head
    for _ in range(new_head_distance_from_current_head - 1):
        new_tail = new_tail.next

    head = new_tail.next
    new_tail.next = None

    return head

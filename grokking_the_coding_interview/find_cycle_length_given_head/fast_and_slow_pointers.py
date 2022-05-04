def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return calculate_cycle_length(slow)
    return 0


def calculate_cycle_length(slow):
    current = slow
    length = 0
    while True:
        current = current.next
        length += 1
        if current == slow:
            break
    return length

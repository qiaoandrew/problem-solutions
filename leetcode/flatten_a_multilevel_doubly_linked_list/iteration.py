def flatten(head):
    if not head:
        return head

    sentinel = Node(None, None, head, None)
    prev = sentinel

    stack = [head]

    while stack:
        cur = stack.pop()

        prev.next = cur
        cur.prev = prev

        if cur.next:
            stack.append(cur.next)

        if cur.child:
            stack.append(cur.child)
            cur.child = None

        prev = cur

    sentinel.next.prev = None
    return sentinel.next

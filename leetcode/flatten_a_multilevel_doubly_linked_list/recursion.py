def flatten(head):

    def flatten_dfs(prev, cur):
        if not cur:
            return prev

        cur.prev = prev
        prev.next = cur

        next_temp = cur.next
        tail = flatten_dfs(cur, cur.child)
        cur.child = None
        return flatten_dfs(tail, next_temp)

    if not head:
        return head

    sentinel = Node(None, None, head, None)
    flatten_dfs(sentinel, head)
    sentinel.next.prev = None
    return sentinel.next

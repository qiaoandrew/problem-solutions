def print_linked_list_in_reverse(head):
    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.getNext()
    nodes.reverse()
    for node in nodes:
        node.printValue()

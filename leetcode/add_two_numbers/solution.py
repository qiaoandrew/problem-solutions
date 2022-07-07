def add_two_numbers(l1, l2):
    sentinel = ListNode(0)
    cur_node = sentinel
    carry = 0

    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        cur_sum = l1_val + l2_val + carry
        carry = cur_sum // 10

        new_node = ListNode(cur_sum % 10)
        cur_node.next = new_node
        cur_node = new_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return sentinel.next

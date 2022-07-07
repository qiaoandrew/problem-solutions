def odd_even_list(head):
    if not head:
        return None

    odds = ListNode(0)
    evens = ListNode(0)
    odds_head = odds
    evens_head = evens
    is_odd = True

    while head:
        if is_odd:
            odds.next = head
            odds = odds.next
        else:
            evens.next = head
            evens = evens.next
        is_odd = not is_odd
        head = head.next

    evens.next = None
    odds.next = evens_head.next
    return odds_head.next

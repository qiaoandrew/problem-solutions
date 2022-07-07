def merge_two_lists(list1, list2):
    sentinel = ListNode(0)
    prev = sentinel

    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    if list1:
        prev.next = list1
    else:
        prev.next = list2

    return sentinel.next

def is_palindrome(head):

    def reverse(head):
        prev = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    if head is None or head.next is None:
        return True

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half

    result = True
    while head is not None and head_second_half is not None:
        if head.val != head_second_half.val:
            result = False
        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)

    return result
## 1. Use slow, fast pointers to find middle of linked list
## 2. Reverse the second half
## 3. Use pointers at head of first half and at head of second half to weave them together
## 4. If there was an odd amount of nodes, the new linked list will terminate on a node from the first half, thus its pointer must be set to none


def reorder_list(head):

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
        return head

    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    cur_first_half = head
    cur_second_half = reverse(slow)
    while cur_first_half is not None and cur_second_half is not None:
        temp = cur_first_half.next
        cur_first_half.next = cur_second_half
        cur_first_half = temp

        temp = cur_second_half.next
        cur_second_half.next = cur_first_half
        cur_second_half = temp

    if cur_first_half is not None:
        cur_first_half.next = None

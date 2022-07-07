class Solution:

    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        return prev

    def is_palindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_second_half = self.reverse(slow)

        while head and head_second_half:
            if head.val != head_second_half.val:
                return False
            head = head.next
            head_second_half = head_second_half.next

        return True
class Solution:

    def get_intersect(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow
        return None

    def detect_cycle(self, head):
        if head is None:
            return None

        intersect = self.get_intersect(head)
        if intersect is None:
            return None

        slow, fast = head, intersect
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow

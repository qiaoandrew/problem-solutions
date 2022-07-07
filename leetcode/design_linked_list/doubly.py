class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        if index * 2 < self.size:
            cur_node = self.head
            for _ in range(index + 1):
                cur_node = cur_node.next
        else:
            cur_node = self.tail
            for _ in range(self.size - index):
                cur_node = cur_node.prev

        return cur_node.val

    def add_at_head(self, val):
        self.add_at_index(0, val)

    def add_at_tail(self, val):
        self.add_at_index(self.size, val)

    def add_at_index(self, index, val):
        if index < 0 or index > self.size:
            return

        if index * 2 < self.size:
            prev_node = self.head
            for _ in range(index):
                prev_node = prev_node.next
            next_node = prev_node.next
        else:
            next_node = self.tail
            for _ in range(self.size - index):
                next_node = next_node.prev
            prev_node = next_node.prev

        new_node = Node(val)
        prev_node.next = new_node
        next_node.prev = new_node
        new_node.prev = prev_node
        new_node.next = next_node

        self.size += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return

        if index * 2 < self.size:
            prev_node = self.head
            for _ in range(index):
                prev_node = prev_node.next
            next_node = prev_node.next.next
        else:
            next_node = self.tail
            for _ in range(self.size - index - 1):
                next_node = next_node.prev
            prev_node = next_node.prev.prev

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1
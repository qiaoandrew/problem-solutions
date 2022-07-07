class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        cur_node = self.head
        for _ in range(index + 1):
            cur_node = cur_node.next
        return cur_node.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        cur_node = Node(val)
        cur_node.next = prev_node.next
        prev_node.next = cur_node

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        prev_node.next = prev_node.next.next

        self.size -= 1
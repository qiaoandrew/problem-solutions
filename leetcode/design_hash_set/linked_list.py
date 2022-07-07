class HashSet:

    def __init__(self):
        self.key_range = 769
        self.bucket_array = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, key):
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].insert(key)

    def remove(self, key):
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].delete(key)

    def contains(self, key):
        bucket_index = self._hash(key)
        return self.bucket_array[bucket_index].exists(key)


class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class Bucket:

    def __init__(self):
        self.head = Node(0)

    def insert(self, new_val):
        if not self.exists(new_val):
            new_node = Node(new_val, self.head.next)
            self.head.next = new_node

    def delete(self, val):
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def exists(self, val):
        cur = self.head.next
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

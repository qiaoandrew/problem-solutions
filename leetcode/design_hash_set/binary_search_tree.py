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


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Bucket:

    def __init__(self):
        self.tree = BSTree()

    def insert(self, val):
        self.tree.root = self.tree.insert(self.tree.root, val)

    def delete(self, val):
        self.tree.root = self.tree.delete(self.tree.root, val)

    def exists(self, val):
        return (self.tree.search(self.tree.root, val) is not None)


class BSTree:

    def __init__(self):
        self.root = None

    def search(self, root, val):
        if not root or val == root.val:
            return root

        return self.search(root.left, val) if val < root.val else self.search(
            root.right, val)

    def insert(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def delete(self, root, val):
        if not root:
            return None

        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.delete(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.delete(root.left, root.val)

        return root

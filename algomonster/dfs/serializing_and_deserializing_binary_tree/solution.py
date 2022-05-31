from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    traverse_list = []

    def dfs(node):
        if node is None:
            traverse_list.append('#')
            return

        traverse_list.append(node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return ' '.join(traverse_list)


def deserialize(s):
    traverse_list = s.split()
    traverse_list = deque(traverse_list)

    def dfs():
        val = traverse_list.popleft()
        if val == '#':
            return

        cur_node = Node(int(val))
        cur_node.left = dfs()
        cur_node.right = dfs()
        return cur_node

    return dfs()

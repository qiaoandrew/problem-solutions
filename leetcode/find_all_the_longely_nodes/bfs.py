from collections import deque


def find_all_the_lonely_nodes(root):
    queue = deque([root])
    lonely_nodes = []
    while queue:
        cur_node = queue.popleft()
        if cur_node.left and not cur_node.right:
            lonely_nodes.append(cur_node.left.val)
        if cur_node.right and not cur_node.left:
            lonely_nodes.append(cur_node.right.val)
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return lonely_nodes
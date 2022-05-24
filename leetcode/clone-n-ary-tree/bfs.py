class Solution:

    def clone_tree(root):
        if not root:
            return root

        node_copy = Node(root.val)
        for child in root.children:
            node_copy.children.append(self.clone_tree(child))

        return node_copy

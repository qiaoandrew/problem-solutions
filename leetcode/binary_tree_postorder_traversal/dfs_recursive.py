class Solution:

    def postorder_traversal(self, root):
        traverse_list = []
        self.dfs(root, traverse_list)
        return traverse_list

    def dfs(self, node, traverse_list):
        if node is not None:
            self.dfs(node.left, traverse_list)
            self.dfs(node.right, traverse_list)
            traverse_list.append(node.val)

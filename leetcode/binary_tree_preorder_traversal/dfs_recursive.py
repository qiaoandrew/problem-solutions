class Solution:

    def preorder_traversal(self, root):
        traverse_list = []
        self.dfs(root, traverse_list)
        return traverse_list

    def dfs(self, cur_node, traverse_list):
        if cur_node:
            traverse_list.append(cur_node.val)
            self.dfs(cur_node.left, traverse_list)
            self.dfs(cur_node.right, traverse_list)

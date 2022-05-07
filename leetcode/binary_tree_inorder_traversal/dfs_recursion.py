class Solution:

    def inorder_traversal(self, root):
        traverse_list = []
        self.dfs(root, traverse_list)
        return traverse_list

    def dfs(self, cur_node, traverse_list):
        if cur_node:
            self.dfs(cur_node.left)
            traverse_list.append(cur_node)
            self.dfs(cur_node.right)

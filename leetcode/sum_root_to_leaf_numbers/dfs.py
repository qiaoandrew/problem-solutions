class Solution:

    def sum_numbers(self, root):
        return self.find_sum(root, 0)

    def find_sum(self, cur_node, cur_sum):
        if cur_node is None:
            return 0

        cur_sum = cur_sum * 10 + cur_node.val

        if cur_node.left is None and cur_node.right is None:
            return cur_sum

        return self.find_sum(cur_node.left, cur_sum) + self.find_sum(
            cur_node.right, cur_sum)

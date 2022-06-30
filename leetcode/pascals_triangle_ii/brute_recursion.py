class Solution:

    def get_num(self, row, col):
        if row == 0 or col == 0 or row == col:
            return 1
        return self.get_num(row - 1, col - 1) + self.get_num(row - 1, col)

    def get_row(self, row_index):
        ans = []
        for i in range(row_index + 1):
            ans.add(self.get_num(row_index, i))
        return ans

class Solution:

    def smallest_common_element(self, mat):
        for num in mat[0]:
            if self.in_other_arrays(mat, num):
                return num
        return -1

    def in_other_arrays(self, mat, num):
        for i in range(len(mat)):
            start, end = 0, len(mat[i]) - 1
            while start <= end:
                mid = (start + end) // 2
                if mat[i][mid] == num:
                    break
                elif mat[i][mid] > num:
                    end = mid - 1
                else:
                    start = mid + 1
            if start > end:
                return False
        return True
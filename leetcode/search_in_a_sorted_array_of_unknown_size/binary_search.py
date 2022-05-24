class Solution:

    def search(self, reader, target):
        start, end = 0, 1
        while reader.get(end) < target:
            new_start = end + 1
            end += (end - start + 1) * 2
            start = new_start
        return self.binary_search(reader, target, start, end)

    def binary_search(self, reader, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid + 1
            elif reader.get(mid) > target:
                end = mid - 1
            else:
                return mid
        return -1

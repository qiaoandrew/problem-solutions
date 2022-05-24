class Solution:

    def search_range(self, nums, target):
        positions = [-1, -1]
        positions[0] = self.find_position(nums, target, False)
        if positions[0] != -1:
            positions[1] = self.find_position(nums, target, True)
        return positions

    def find_position(self, nums, target, is_finding_max):
        index = -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                index = mid
                if is_finding_max:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return index
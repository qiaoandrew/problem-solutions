class Solution:

    def search_range(self, nums, target):
        positions = [-1, -1]
        positions[0] = self.find_bound(nums, target, True)
        if positions[0] != -1:
            positions[1] = self.find_bound(nums, target, False)
        return positions

    def find_bound(self, nums, target, is_finding_first):
        left, right = 0, len(nums) - 1
        boundary_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                boundary_index = mid
                if is_finding_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return boundary_index
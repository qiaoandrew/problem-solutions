def max_sum_two_no_overlap(nums, first_len, second_len):

    def max_sum(first, second):
        sum_first = sum_second = 0
        for i in range(first + second):
            if i < first:
                sum_first += nums[i]
            else:
                sum_second += nums[i]
        max_first, total_sum = sum_first, sum_first + sum_second
        for i in range(first + second, len(nums)):
            sum_first += nums[i - second] - nums[i - first - second]
            max_first = max(max_first, sum_first)
            sum_second += nums[i] - nums[i - second]
            total_sum = max(total_sum, max_first + sum_second)
        return total_sum

    return max(max_sum(first_len, second_len), max_sum(second_len, first_len))

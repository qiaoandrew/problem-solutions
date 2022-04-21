def find_disappeared_numbers(nums):
    hash_table = {}
    for num in nums:
        hash_table[num] = 1
    disappeared = []
    for num in range(1, len(nums) + 1):
        if num not in hash_table:
            disappeared.append(num)
    return disappeared

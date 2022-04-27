def contains_duplicates(nums):
    hash_table = {}
    for num in nums:
        if num in hash_table:
            return True
        else:
            hash_table[num] = 1
    return False

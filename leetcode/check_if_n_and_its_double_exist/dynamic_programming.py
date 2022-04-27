def check_if_exist(arr):
    hash_table = {}
    for num in arr:
        if num * 2 in hash_table or num / 2 in hash_table:
            return True
        if num not in hash_table:
            hash_table[num] = 0
    return False

def xor_operation(n, start):
    nums = [start + n * 2 for n in range(n)]
    ans = 0

    for num in nums:
        ans = ans ^ num
    return ans

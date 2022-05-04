def is_happy(n):
    sums = set()
    cur_num = n
    while True:
        cur_sum = 0
        while cur_num > 0:
            cur_sum += ((cur_num % 10)**2)
            cur_num //= 10
        if cur_sum == 1:
            return True
        elif cur_sum in sums:
            return False
        else:
            sums.add(cur_sum)
            cur_num = cur_sum


print(is_happy(2))
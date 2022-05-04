def is_happy(n):

    def get_next(num):
        total_sum = 0
        while num > 0:
            total_sum += (num % 10)**2
            num //= 10
        return total_sum

    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1
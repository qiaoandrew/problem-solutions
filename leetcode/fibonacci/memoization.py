def fib(n):
    cache = {0: 0, 1: 1}

    def helper(n):
        if n in cache:
            return cache[n]
        cache[n] = helper(n - 1) + helper(n - 2)
        return cache[n]

    return helper(n)

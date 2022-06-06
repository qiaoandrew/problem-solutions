def fib(n):

    def helper(n, memo):
        if n in memo:
            return memo[n]

        if n == 0 or n == 1:
            return n

        res = fib(n - 1, memo) + fib(n - 2, memo)
        memo[n] = res

        return res

    return helper(n, {})
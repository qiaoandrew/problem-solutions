def palindrome_counting(s):
    length = len(s)
    dp = [[False for _ in range(length)] for _ in range(length)]
    ans = 0

    for cur_length in range(1, length + 1):
        for start in range(length - cur_length + 1):
            end = start + cur_length - 1
            if (cur_length <= 2
                    or dp[start + 1][end - 1]) and s[start] == s[end]:
                dp[start][end] = True
                ans += 1

    return ans
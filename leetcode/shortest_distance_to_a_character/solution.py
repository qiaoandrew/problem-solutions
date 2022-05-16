def shortest_to_char(s, c):
    ans = []
    prev = -float('inf')
    for i in range(len(s)):
        if s[i] == c:
            prev = i
        ans.append(i - prev)
    prev = float('inf')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev = i
        ans[i] = min(ans[i], prev - i)
    return ans

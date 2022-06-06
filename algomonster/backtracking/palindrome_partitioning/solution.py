def partition(s):
    ans = []

    def is_palindrome(s):
        return s == s[::-1]

    def dfs(start_index, cur_path):
        if start_index == len(s):
            ans.append(cur_path[:])
            return

        for i in range(start_index + 1, len(s) + 1):
            prefix = s[start_index:i]
            if is_palindrome(prefix):
                dfs(i, cur_path + [prefix])

    dfs(0, [])
    return ans
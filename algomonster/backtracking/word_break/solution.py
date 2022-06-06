def word_break(s, words):
    memo = {}

    def dfs(start_index):
        if start_index == len(s):
            return True

        if start_index in memo:
            return memo[start_index]

        index_possible = False

        for word in words:
            if s[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    index_possible = True
                    break

        memo[start_index] = index_possible
        return index_possible

    return dfs(0)

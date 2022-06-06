def permutations(letters):

    def dfs(path, used, res):
        if len(path) == len(letters):
            res.append(''.join(path))
            return

        for i in range(len(letters)):
            if used[i]:
                continue
            path.append(letters[i])
            used[i] = True
            dfs(path, used, res)
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(letters), res)
    return res

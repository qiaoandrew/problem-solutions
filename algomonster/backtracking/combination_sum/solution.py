def combination_sum(candidates, target):
    res = []

    def dfs(start_index, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return

        for i in range(start_index, len(candidates)):
            if remaining - candidates[i] < 0:
                continue
            dfs(i, remaining - candidates[i], path + [candidates[i]])

    dfs(0, target, [])
    return res

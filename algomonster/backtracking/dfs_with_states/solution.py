def ternary_tree_paths(root):

    def dfs(node, cur_path, paths):
        if all(child is None for child in node.children):
            paths.append('->'.join(cur_path) + '->' + str(node.val))
            return

        for child in node.children:
            if child is not None:
                cur_path.append(str(node.val))
                dfs(child, cur_path, paths)
                cur_path.pop()

    paths = []
    if root:
        dfs(root, [], paths)
    return paths
from collections import defaultdict


def find_duplicate_subtrees(root):

    def tuplify(root):
        if root:
            tuple = root.val, tuplify(root.left), tuplify(root.right)
            trees[tuple].append(root)
            return tuple

    trees = defaultdict(list)
    tuplify(root)
    return [roots[0] for roots in trees.values() if len(roots) > 1]

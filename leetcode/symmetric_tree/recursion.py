def is_symmetric(root):

    def helper(n1, n2):
        if n1 is None and n2 is None:
            return True
        elif n1 is None or n2 is None:
            return False
        else:
            return n1.val == n2.val and helper(n1.left, n2.right) and helper(
                n2.right, n1.left)

    return helper(root, root)

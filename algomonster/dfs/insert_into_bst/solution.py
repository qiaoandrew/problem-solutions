def insert_bst(bst, val):
    if bst is None:
        return Node(val)
    if bst.val < val:
        bst.right = insert_bst(bst.right, val)
    elif bst.val > val:
        bst.left = insert_bst(bst.left, val)
    return bst

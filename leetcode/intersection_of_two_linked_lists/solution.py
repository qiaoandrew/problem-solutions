def get_intersect_node(head_a, head_b):
    p_a, p_b = head_a, head_b
    while p_a != p_b:
        p_a = head_b if p_a is None else p_a.next
        p_b = head_a if p_b is None else p_b.next
    return p_a
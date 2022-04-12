def backspace_compare(s, t):
    p_s = len(s) - 1
    p_t = len(t) - 1
    while p_s >= 0 or p_t >= 0:
        if (p_s >= 0 and s[p_s] == '#') or (p_t >= 0 and t[p_t] == '#'):
            if p_s >= 0 and s[p_s] == '#':
                backcount = 2
                while backcount > 0:
                    p_s -= 1
                    backcount -= 1
                    if p_s >= 0 and s[p_s] == '#':
                        backcount += 2

            if p_t >= 0 and t[p_t] == '#':
                backcount = 2
                while backcount > 0:
                    p_t -= 1
                    backcount -= 1
                    if p_t >= 0 and t[p_t] == '#':
                        backcount += 2
        else:
            if p_s >= 0 and p_t >= 0:
                if s[p_s] != t[p_t]:
                    return False
                else:
                    p_s -= 1
                    p_t -= 1
            else:
                return False
    return True


print(backspace_compare('##', '##'))
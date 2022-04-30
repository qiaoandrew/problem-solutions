def valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for parentheses in s:
        if parentheses in pairs:
            if stack and stack[-1] == pairs[parentheses]:
                stack.pop()
            else:
                return False
        else:
            stack.append(parentheses)
    return False if stack else True

def longest_nice_substring(s):
    ans = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            has_counterpart = 0
            for letter in substring:
                if letter.lower() in substring and letter.upper() in substring:
                    has_counterpart += 1
            if has_counterpart == len(substring):
                ans = max(ans, substring, key=len)
    return ans
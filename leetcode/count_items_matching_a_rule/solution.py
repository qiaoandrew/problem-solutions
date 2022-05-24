def count_matches(items, rule_key, rule_value):
    rule_index = 0
    if rule_key == 'type':
        rule_index = 0
    elif rule_key == 'color':
        rule_index = 1
    else:
        rule_index = 2

    counter = 0
    for item in items:
        if item[rule_index] == rule_value:
            counter += 1
    return counter
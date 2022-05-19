def kids_with_candies(candies, extraCandies):
    max_candies = 0
    for num in candies:
        max_candies = max(max_candies, num)
    result = []
    for num in candies:
        result.append(num + max_candies > max_candies)
    return result

def subtract_product_and_sum(n):
    temp = n
    product = 1
    sum = 0
    while temp > 0:
        digit = temp % 10
        product *= digit
        sum += digit
        temp /= 10
    return product - sum
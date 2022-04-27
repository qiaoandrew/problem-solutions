def product_except_self(nums):
    products = [1] * len(nums)
    prefix_product = 1
    for i in range(len(nums)):
        products[i] = prefix_product
        prefix_product *= nums[i]
    suffix_product = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= suffix_product
        suffix_product *= nums[i]
    return products


print(product_except_self([-1, 1, 0, -3, 3]))

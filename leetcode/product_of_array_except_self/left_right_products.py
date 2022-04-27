def product_except_self(nums):
    prefix = [1] * len(nums)
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    suffix = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    products = []
    for i in range(len(nums)):
        products.append(prefix[i] * suffix[i])
    return products


print(product_except_self([-1, 0]))

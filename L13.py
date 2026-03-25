def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    sum_nums = sum(nums)
    return total - sum_nums
def find_pair(nums, target):
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)

    return None
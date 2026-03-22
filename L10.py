from itertools import combinations

def get_subsets(nums):
    subsets = []
    for r in range(len(nums) + 1):
        subsets.extend(combinations(nums, r))
    return subsets

print(get_subsets([1, 2, 3]))
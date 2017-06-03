def two_sum(nums, target):
    if len(nums) == 0 and target == 0:
        raise ValueError
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

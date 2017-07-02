def two_sum(nums, target):
    sum_of_numbers = []
    if len(nums) == 0 and target == 0:
        raise ValueError
    for num1 in range(len(nums)):
        for num2 in range(len(nums)):
            if (nums[num1] + nums[num2]) == target:
                sum_of_numbers.append(num1)
    return sum_of_numbers

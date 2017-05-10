def build( nums, target):
    if nums is None or target is None:
        return False
    if not nums:
        return False
    cache = {}
    for index, num in enumerate(nums):
        cache_target = target - num
        if num in cache:
            return [cache[num], index]
        else:
            cache[cache_target] = index
    return False

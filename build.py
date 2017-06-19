import itertools

def two_sum(nums, thesum):
    result = []
    if nums==None or thesum==None:
        raise TypeError
    if nums == [] or thesum==0:
        raise ValueError
    for a,b in itertools.combinations(nums, 2):
        if a+b == thesum:
            result.append(nums.index(a))
            result.append(nums.index(b))

    return result

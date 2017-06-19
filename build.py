import itertools

def two_sum(numbers, target):
    if numbers is None or target is None:
        raise TypeError('Input numbers must be a list and target should be integer')
    if numbers == [] or target == 0:
        raise ValueError('Input list shouldn\'t not be empty ')

    pairs = list(itertools.combinations(numbers, 2))
    pair_sums = [sum(pair) for pair in pairs]
    indexes = [numbers.index(num) for num in pairs[pair_sums.index(target)]]

    return indexes

print(two_sum([1, 3, 2, -7, 5], 7))

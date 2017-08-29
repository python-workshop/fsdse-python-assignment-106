def two_sum(values, n):
    if values is None:
        raise TypeError()
    if  values == []:
        raise ValueError()

    for i, a in enumerate(values):
        for j, b in enumerate(values[i + 1: ]):
            if a + b == n:
                return [i, j + i + 1]

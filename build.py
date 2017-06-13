def two_sum(n, m):
    if len(n) == 0 and m == 0:
        raise ValueError
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i]+n[j] == m:
                return [i,j]

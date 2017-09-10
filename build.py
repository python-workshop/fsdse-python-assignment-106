def two_sum(a, b):
    if len(a) < 2:
        raise ValueError
    for x in range(len(a)):
		for j in range(len(a)):
			if a[x] + a[j] == b:
				ans = x, j
				return list(ans)

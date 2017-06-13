def two_sum(num, sum):
    if len(num) == 0 and sum == 0:
        raise ValueError
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i]+num[j] == sum:
                return [i,j]
print(two_sum([0,2,3,4,5],5))

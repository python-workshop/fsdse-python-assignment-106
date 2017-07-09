def two_sum(lst,total):

    if(lst == [] and total == 0):
        raise ValueError

    final =[]

    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i] + lst[j] == total:
                final.append(i)
                final.append(j)

    return final

def two_sum(l1,num):
    if l1 == []:
        raise ValueError
    elif l1 == None:
        raise TypeError
    else:
        for i in range(0,len(l1)):
            for j in range(0,len(l1)):
                if l1[i] + l1[j] == num and i !=j:
                    return [i,j]

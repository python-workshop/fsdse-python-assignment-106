def two_sum(a_list, n):
    if a_list is None:
        raise TypeError("Inputs can't be None")
    if  a_list == []:
        raise ValueError("Input list can't be empty")

    for a in a_list:
        for b in a_list[a_list.index(a):]:
            if a + b == n:
                return [a_list.index(a), a_list.index(b)]

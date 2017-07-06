def two_sum(mylist, total):
    if mylist is None or total is None:
        raise TypeError("invalid input")
    if len(mylist) == 0:
        raise ValueError("empty list has no solution")

    hash_map = [0]*len(mylist)
    for i, num in enumerate(mylist):
        if (total-num) in mylist[i+1:]:
            other_number= total-num
            return [i, mylist.index(other_number)]

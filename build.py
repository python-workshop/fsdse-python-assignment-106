def two_sum(arg_list, arg_number):
    if arg_list is None:
        raise TypeError
    elif arg_list == []:
        raise ValueError
    else:
        pass

    for x,y in enumerate(arg_list):
        for k,l in enumerate(arg_list):
            if y + l == arg_number:
                return [x, k]
    return None

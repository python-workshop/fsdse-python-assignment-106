def two_sum(arg_list, arg_number):
    try:
        type(arg_list) is list
        type(arg_number) is str
        int(arg_number)
        arg_list[0] is not None
    except TypeError:
        raise TypeError
    except ValueError:
        raise ValueError
    except IndexError:
        raise ValueError

    output = []
    for x,y in enumerate(arg_list):
        for k,l in enumerate(arg_list):
            if y + l == arg_number:
                output.append(x)
                output.append(k)
                return output
    return None


print two_sum([1, 3, 2, -7, 5], 7)

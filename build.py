def two_sum(arr,sum):
    arrDict = {}
    if arr is None:
        raise TypeError
    elif len(arr) == 0:
        raise ValueError
    else:
        for i in range(0,len(arr)):
            arrDict[arr[i]] = arr[i]
            if sum-arr[i] in arrDict:
                return list([arr.index(sum-arr[i]),i])

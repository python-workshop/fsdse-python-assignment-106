def two_sum(nums,target):
    sums = []

    if nums == None or target == None:
        print "Raising Type Error"
        raise TypeError
    elif not nums or target == 0:
        print "Raising Value Error"
        raise ValueError

    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                sums.extend((i,j))
    return sums

#nums = [1, 3, 2, -7, 5]
#target = 7
#two_sum(nums,target)

def two_sum(list1,temp1):
    list2 =[]
    if len(list1) == 0 and temp1 == 0:
         raise ValueError
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            if list1[i]+ list1[j] == temp1:
                list2.append(i)
                list2.append(j)
    return list2

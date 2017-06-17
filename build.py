def two_sum(inputList,Sum):
    ''' to get the two indices that sum to a specific value. '''
    if(inputList == [] and Sum == 0):
        raise ValueError

    indicesList = []
    for i in range (0,len(inputList)):
        for j in range (i+1,len(inputList)):
            if(inputList[i] + inputList[j] == Sum):
                indicesList.extend((i,j))
    print indicesList
    return indicesList

two_sum([9,12,5,1,13,18,-12,20,7], 16)

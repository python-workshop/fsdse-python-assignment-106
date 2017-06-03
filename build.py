def two_sum(inputList,Sum):

    if(inputList == [] and Sum == 0):
        raise ValueError

    indicesList = []
    for i in range (0,len(inputList)):
        for j in range (i+1,len(inputList)):
            if(inputList[i] + inputList[j] == Sum):
                indicesList.extend((i,j))

    return indicesList

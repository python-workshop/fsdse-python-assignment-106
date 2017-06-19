def two_sum(li,number):
    if(li==None and number==None):
        raise TypeError('Type error')
    if(li==[] and number==0):
        raise ValueError('Value error')
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(li[i]+li[j]==number):
                return [i,j]
#print two_sum([1,5,2,8],13)
#print two_sum([],2)

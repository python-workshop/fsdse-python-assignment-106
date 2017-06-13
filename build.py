def two_sum(l,sum):
    list=[]
    if l==None or sum==None:
        raise TypeError
    if not l or sum==0:
        raise ValueError
    for x in range(0,len(l)-1):
        for y in range(x+1,len(l)):
            if l[x]+l[y]==sum:
                list.extend([x,y])
    return list
print two_sum([9,12,5,1,13,18,-12,20,7], 16)

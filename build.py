def two_sum(ls, ex_sum):
    if (ls == None) or (ex_sum==None):
        raise TypeError
    if len(ls)==0 or ex_sum==0:
        raise ValueError
    seen = set()
    op_ls = []
    for ele1 in ls:
        for ele2 in ls:
            if ele1+ele2 == ex_sum:
                print(ele1,ele2)
                index1 = ls.index(ele1)
                index2 = ls.index(ele2)
                seen.add(index1)
                seen.add(index2)
    return list(seen)


#print two_sum([1,3,2,-7,5],7)
#two_sum(None,None)
#print (a,type(a))

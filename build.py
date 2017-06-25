ls = [9,12,5,1,13,18,-12,20,7]
num = 16

def two_sum(l1,temp):
    l2 =[]
    if len(l1) == 0:
         raise ValueError
    for i in range(len(l1)):
        for j in range(i,len(l1)):
            if l1[i]+ l1[j] == temp:
                l2.append(i)
                l2.append(j)
    return l2

# two_sum(ls,num)
# Output : [0, 8]

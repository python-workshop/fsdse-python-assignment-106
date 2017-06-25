ls = [9,12,5,1,13,18,-12,20,7]
num = 16

def two_sum(ls,num):
    if len(ls) == 0:
         raise ValueError
    ls1 = []
    for i, item in enumerate(ls):
        for j in range(i, len(ls)):
            if ls[i] + ls[j] == num:
                ls1.append(i)
                ls1.append(j)
    return ls1

# two_sum(ls,num)
# Output : [0, 8]

def two_sum(list_a,num):
    if list_a == None:
        raise TypeError
    elif list_a == []:
        raise ValueError
    else:
        b=[]
        for i in range(len(list_a)):
              for j in range(i+1, len(list_a)):
                    if((list_a[i]+list_a[j]) == num):
                        b.append(i)
                        b.append(j)
        return b

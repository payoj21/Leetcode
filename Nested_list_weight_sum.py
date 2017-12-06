def depthSum(nestedList):

    tot_sum = 0


    sum_list = []
    if len(nestedList) == 0:
        return 0
    for i in nestedList:
        sum_list.append((i,1))

    while sum_list:
        element,depth = sum_list.pop(0)

        if element.isInteger():
            tot_sum += depth*element.getInteger()
        else:
            for index in element.getList():
                sum_list.append((index,depth+1))

    return tot_sum
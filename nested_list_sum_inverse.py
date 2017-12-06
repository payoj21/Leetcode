def depthSumInverse(nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    stck = []
    depth_max = 1
    if nestedList ==[]:
        return 0
    for i in nestedList:
        stck.append((i, 1))

    def depth(stck_list, stck_depth):

        list_stack = []
        while (stck_list):
            element, depth = stck_list.pop()

            result = isinstance(element, int)
            if result == True:
                list_stack.append((element,depth))
            else:

                depth += 1
                if depth > stck_depth:
                    stck_depth = depth
                for each_element in element:
                    stck_list.append((each_element, depth))
        return list_stack, stck_depth

    depth_list,max_depth_len = depth(stck, depth_max)
    print(depth_list, max_depth_len)
    result = 0
    for i,d in depth_list:
        result += i*(max_depth_len-d+1)

    return result

print(depthSumInverse([1,[4,[6]]]))
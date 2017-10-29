def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0
    if len(nums) == 1:
        return 1

    rep_ele = nums[0]
    length = len(nums)
    repitition_index = 1
    for index in range(1, len(nums)):
        if nums[index] == rep_ele:
            length -= 1
        else:
            rep_ele = nums[index]
            nums[repitition_index] = nums[index]
            repitition_index += 1
    return length

print(removeDuplicates([1,2,3]))
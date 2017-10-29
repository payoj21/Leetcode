def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    val = n

    string_int = []

    while(val>0):
        string_int.append(val%26)
        val = int(val/26)
    string =''
    for index in range(len(string_int)-1,-1,-1):
        string += chr(64+string_int[index])

    return string

print(convertToTitle(1))
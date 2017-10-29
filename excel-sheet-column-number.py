def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.lower()
    length = len(s)
    val = 0
    for index in range(length):
        val = val + (ord(s[index]) - 96) * (26 ** (length - index - 1))

    return val

print(titleToNumber('A'))

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    string = ''
    for st in s:
        if st.isalnum():
            string += st

    for index in range(int(len(string) / 2)):
        if string[index] != string[len(string) - index - 1]:
            return False
    return True


print(isPalindrome(""))
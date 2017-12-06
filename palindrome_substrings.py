def substrings(s):
    length = 1
    substring = []
    while (length <= len(s)):
        for i in range(len(s)-length+1):
            substring.append(s[i:i + length])
        length += 1
    return substring

print(substrings("aaa"))


def palindrome(s):
    i = 0
    j = len(s)-1
    while (i<=j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

print(palindrome("aaa"))
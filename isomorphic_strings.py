def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    mapping = dict()
    repeat = dict()
    for i in range(len(s)):
        if s[i] in mapping:
            if t[i] == mapping[s[i]]:
                continue
            else:
                return False
        else:
            if t[i] in repeat:
                return False
            else:
                mapping.update({s[i]: t[i]})
                repeat.update({t[i]:1})

    return True

#ord () gives number value of a char
#chr () gives char of a number
def isIsomorphic2(s,t):

    d1 = [0]*256
    d2 = [0]*256
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] += 1
        d2[ord(t[i])] += 1

    return True


print(isIsomorphic2('aa','ab'))
def minimumDeleteSum(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: int
    """
    # ascii_1 = [ord(s1[0])]
    # ascii_2 = [ord(s2[0])]
    #
    # for index in range(1,len(s1)):
    #     x = ascii_1[len(ascii_1)-1]
    #     ascii_1.append(x+ord(s1[index]))
    #
    # for index in range(1,len(s2)):
    #     x = ascii_2[len(ascii_2)-1]
    #     ascii_2.append(x+ord(s2[index]))
    #
    # print(ascii_1,ascii_2)
    #
    # lcs_ascii = 0
    #
    # i = len(s1)-1
    # j = len(s2)-1
    # s = []
    #
    # while(i >=0 and j >=0):
    #     print(i,j, s1[i],s2[j])
    #     if s1[i] == s2[j]:
    #         lcs_ascii += ord(s1[i])
    #         s.append(s1[i])
    #         i -= 1
    #         j -= 1
    #     else:
    #         if ascii_1[i] > ascii_2[j]:
    #             i -= 1
    #         else:
    #             j -= 1
    # print(lcs_ascii,s)
    #
    # return ascii_1[len(ascii_1)-1] + ascii_2[len(ascii_2)-1] - (2*lcs_ascii)
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + ord(s1[i]) * 2
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    n1 = sum(ord(c) for c in s1)
    n2 = sum(ord(c) for c in s2)
    return n1 + n2 - dp[l1][l2]

print(minimumDeleteSum('delete','leet'))
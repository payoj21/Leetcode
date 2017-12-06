import math


def shortestDistance(words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    word_dictionary = dict()

    for index, w in enumerate(words):
        if w in word_dictionary:
            word_dictionary[w].append(index)
        else:
            word_dictionary.update({w:[index]})
    print(word_dictionary)
    arr_word1 = word_dictionary[word1]
    arr_word2 = word_dictionary[word2]
    print(arr_word1, arr_word2)
    if len(arr_word1) == 0 or len(arr_word2) == 0:
        return -1

    else:
        j = 0
        minimum = float('inf')
        while( j< len(arr_word2)):
            for i in range(len(arr_word1)):
                if abs(arr_word2[j] - arr_word1[i]) < minimum:
                    minimum = abs(arr_word2[j] - arr_word1[i])
            j +=1

    return minimum


def shortestDistance1(words, word1, word2):
    size = len(words)
    index1, index2 = size, size
    ans = size

    for i in range(size):
        if words[i] == word1:
            index1 = i
            ans = min(ans, abs(index1 - index2))
        elif words[i] == word2:
            index2 = i
            ans = min(ans, abs(index1 - index2))
    return ans


distance = shortestDistance1(["a", "c", "b", "a"], "b", "a")
print(distance)
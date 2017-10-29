import math
import sys
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    difference = 0
    min = prices[0]
    for i in range(1,len(prices)):
        if prices[i] > min:

            if prices[i] - min > difference:
                difference = prices[i] - min
        else:
            min = prices[i]
    return difference
print(maxProfit([7, 1, 5, 3, 6, 4]))
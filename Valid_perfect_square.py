def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def primes(n):
    primes_list = []
    for i in range(2, int(n / 2) + 1):
        if isPrime(i) == True:
            primes_list.append(i)
    return primes_list


def factors(num):
    n = num
    list = primes(n)
    power = dict()
    for i in list:
        power.update({i: 0})

    for i in list:
        while (n) > 1:

            if n % i == 0:
                power[i] += 1
                n = n / i
            else:
                break
        return power


def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    powers = factors(num)
    count = 0
    for i in powers:
        if powers[i] != 0:
            if powers[i] % 2 != 0:
                return False
        else:
            count += 1
    if count == len(powers):
        return False
    return True


def isPerfectSquare1(num):
    for i in range(int(num/2)):
        if i*i == num:
            return True
    return False

def isPerfectSquare2(num):
    l =0
    r = num
    while(l<=r):
        mid = l + r >>1
        sqmid = mid*mid
        if sqmid > num :
            r = mid -1
        else:
            if sqmid < num :
                l = mid +1
            else: return True
    return False

print(isPerfectSquare2(2147483647))
def canPlaceFlowers(flowerbed,n):

    def consecutivethreezeros(arr):
        count = 0
        i = 3
        if len(arr) < i:
            if arr[0] == 0:
                count += 1
            return count
        else:
            if arr[0] == 0 and arr[1] == 0:
                count = count + 1
            if arr[len(arr) - 1] == 0 and arr[len(arr) - 2] == 0:
                count = count + 1

            while (i < len(arr) - 1):
                if arr[i] == 0 and arr[i - 1] == 0 and arr[i - 2] == 0:
                    count = count + 1
                    i += 2
                else:
                    i += 1
            return count

    emptyspots = consecutivethreezeros(flowerbed)
    if emptyspots >= n:
        return True
    return False


print(canPlaceFlowers([0,0],1))
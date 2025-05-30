def mySqrt(x):
    if x == 1:
        return 1
    low, high = 0, x - 1
    while low < high:
        mid = (low + high)//2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            high = mid - 1
        else:
            low = mid + 1
    if low * low > x:
        return low - 1
    return low

print(mySqrt(8))
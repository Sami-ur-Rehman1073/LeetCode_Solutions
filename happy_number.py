def isHappy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        sum_of_squares = 0
        x = str(n)
        for i in x:
            sum_of_squares += int(i) ** 2
        n = sum_of_squares
    return True
print(isHappy(2))
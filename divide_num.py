def divide(dividend, divisor):
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1 
    if divisor == 1:
        return dividend
    if divisor == -1:
        return -(dividend)
    positive_dividend = abs(dividend)
    positive_divisor = abs(divisor)

    powers_list = []
    while positive_divisor <= positive_dividend:
        i = 0
        while (positive_divisor*(2**i)) <= positive_dividend:
            power_of_two = 2**i
            i += 1
        powers_list.append(power_of_two)
        positive_dividend = positive_dividend - positive_divisor * power_of_two
        
    ans = sum(powers_list)
    if ((dividend > 0) and (divisor > 0)) or ((dividend < 0) and (divisor < 0)):
        return ans
    else:
        return -(ans)

    
print(divide(-60, 12))
    
        


    
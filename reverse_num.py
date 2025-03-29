def reverse(x):
    if x < -2**31 or x > (2**31-1):
        return 0
    elif x >= 0:
        str_num = str(x)
        reversed_str_num = str_num[::-1]
        if int(reversed_str_num) < 2**31-1:
            return int(reversed_str_num)
        else:
            return 0
    elif x < 0:
        positive_num = str(abs(x))
        reversed_positive_num = positive_num[::-1]
        final_num = "-" + reversed_positive_num
        if int(final_num) > -2**31-1:
            return int(final_num)
        else:
            return 0
    
print(reverse(1534236469))

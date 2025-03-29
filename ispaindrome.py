
def isPalindrome(x):
    str_num = str(x)
    str_num_reverse = str_num[::-1]
    if str_num == str_num_reverse:
        return True
    return False

print(isPalindrome(121))
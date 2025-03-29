def isPalindrome(s):
    sentence = ""
    for i in s:
        if i.isalpha():
            sentence += i.lower()
        if i.isdigit():
            sentence += i

    if sentence == sentence[::-1]:
        return True 
    return False

print(isPalindrome("A man, a plan, a canal: Panama"))
def findTheDifference(s, t):
    sum_s = sum_t = 0
    for i in range(len(s)):
        sum_s += ord(s[i])
        sum_t += ord(t[i])
    sum_t += ord(t[len(t) - 1])
    return chr(sum_t - sum_s)
    


print(findTheDifference("abcd", "abcde"))
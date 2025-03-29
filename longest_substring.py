def longest_substring(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    str_len = []
    string_set = set()
    left = 0
    for right in range(len(s)):
        if s[right] in string_set:
            str_len.append(len(string_set))
            while s[right] in string_set:
                string_set.remove(s[left])
                left += 1
        string_set.add(s[right])  
    str_len.append(len(string_set))
    max_len = max(str_len)
    return max_len

print(longest_substring("pwwkew"))




        
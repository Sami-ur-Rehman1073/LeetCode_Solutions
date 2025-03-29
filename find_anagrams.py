from collections import Counter
def findAnagrams(s, p):
    result = []
    y = len(p)
    p_count = Counter(p)
    s_count = Counter(s[:y])

    if p_count == s_count:
        result.append(0)

    for i in range(y, len(s)):
        s_count[s[i]] += 1
        s_count[s[i - y]] -= 1

        if s_count[s[i - y]] == 0:
            del s_count[s[i - y]]

        if s_count == p_count:
            result.append(i - y + 1)

    return result
print(findAnagrams("abab", "ab")) 
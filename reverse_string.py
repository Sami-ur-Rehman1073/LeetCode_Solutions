                # two pointer approach 

def reverseString(s):
    low = 0; high = len(s) - 1
    while low <= high: 
        s[low], s[high] = s[high], s[low] 
        low += 1
        high -= 1
    return s

print(reverseString(["h","e","l","l","o"]))

                # built-in function

def reverseString(s):
    s[:] = s[::-1]
    return s

print(reverseString(["h","e","l","l","o"]))
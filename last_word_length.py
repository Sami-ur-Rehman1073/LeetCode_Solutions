def lengthOfLastWord(s):
    x = s.split()
    return len(x[len(x)-1])

print(lengthOfLastWord("Hello World"))  
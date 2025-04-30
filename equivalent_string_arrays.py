def arrayStringsAreEqual(word1, word2):
    w1 = "".join(word1)
    w2 = "".join(word2) 
    if w1 == w2:
        return True
    return False

print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
    
        
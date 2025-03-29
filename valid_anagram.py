def isAnagram(s, t):

    if sorted(s) == sorted(t):
        return True 
    return False

print(isAnagram( "nagaram" ,  "anagram"))

 
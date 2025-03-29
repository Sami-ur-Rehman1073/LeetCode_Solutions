from collections import Counter
def canConstruct(ransomNote, magazine):
    ransom_counter = Counter(ransomNote)
    magazine_counter = Counter(magazine)
    
    for i in ransom_counter.keys():
        if i not in magazine_counter.keys() or ransom_counter[i] > magazine_counter[i]:
            return False
    return True
    



print((canConstruct("bb", "aab")))
        
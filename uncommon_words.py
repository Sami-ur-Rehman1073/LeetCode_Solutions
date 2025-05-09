from collections import Counter
def uncommonFromSentences(s1, s2):
    result = []
    w_s1 = s1.split(" ")
    w_s2 = s2.split(" ")
    words = Counter(w_s1 + w_s2)
    for i in words.keys():
        if words[i] == 1:
            result.append(i)
    return result

 

print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
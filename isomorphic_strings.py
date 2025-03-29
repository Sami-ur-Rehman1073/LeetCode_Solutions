def isIsomorphic(s, t):
    first_way = {}
    second_way = {}
    
    for i in range(len(s)):
        c1, c2 = s[i], t[i]

        if c1 in first_way.keys() and first_way[c1] != c2:
            return False
        if c2 in second_way.keys() and second_way[c2] != c1:
            return False

        first_way[c1] = c2
        second_way[c2] = c1
    

    return True
        
print(isIsomorphic("foo", "bar"))
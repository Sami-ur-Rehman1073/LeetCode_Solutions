def groupAnagrams(strs):
    hashmap = {}

    for i in strs:
        x = "".join(sorted(i))
        hashmap[x] = []

    for i in strs:
        x = "".join(sorted(i))
        hashmap[x].append(i)
    
    result = [i for i in hashmap.values()]
    return result




print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  

def longestCommonPrefix(strs):
    res = ""
    t = min(strs, key= len)
    j = 0
    for c in t:
        for i in range(len(strs)):
            if strs[i][j] != c :
                return res
        j+=1
        res+=c
    return res
    
  


    

print(longestCommonPrefix(["flower","flow","flight"]))
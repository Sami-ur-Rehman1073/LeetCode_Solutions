def frequencySort(nums):
    from collections import Counter
    
    freq = Counter(nums)  
    print(freq)
    sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
    return sorted_nums



print(frequencySort([2,3,1,3,2]))
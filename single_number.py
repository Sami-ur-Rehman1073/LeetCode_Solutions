
                # by using bit manipulation

def singleNumber(nums):
    res = 0 
    for i in nums:
        res ^= i
    return res

print(singleNumber([2,2,1]))

                # by using hashmap


from collections import Counter
def singleNumber(nums):
    hashmap = Counter(nums)
    for i in nums:
        if hashmap[i] == 1:
            return i 

print(singleNumber([2,2,1]))
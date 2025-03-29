
def removeDuplicates(nums):
    i = j = 1
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
            k += 1
        i += 1
    return j
    

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
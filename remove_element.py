def removeElement(nums, val):
    if nums == []:
        return 0 
    i = 0
    n = len(nums)
    while i != n:
        x = nums[i]
        if x == val:
            nums[i] = nums[n-1]
            n -= 1
        if x != val:
            i += 1
    return n, nums
    

print(removeElement([4], 3))            
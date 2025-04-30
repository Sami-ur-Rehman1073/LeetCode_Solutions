def maximumGap(nums):
    nums.sort()
    
    max_gap = 0
    for i in range(1,len(nums)):
        x = nums[i] - nums[i - 1]
        if  x > max_gap:
            max_gap = x
    return max_gap 

    
print(maximumGap([3,6,9,1]))
        
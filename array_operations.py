def applyOperations(nums):
    low = 0
    high = len(nums) - 1
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i] * 2
            nums[i+1] = 0
    k = nums.count(0)
    nums = [x for x in nums if x != 0]
    nums.extend([0]*k)
    return nums
    

print(applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))  
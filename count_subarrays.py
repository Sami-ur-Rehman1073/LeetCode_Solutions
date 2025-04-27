def countSubarrays(nums):
    count = 0
    for i in range(1, len(nums)-1):
        print(nums[i])
        if (nums[i-1] + nums[i + 1] == nums[i] / 2):
            count += 1
    return count 
    

print(countSubarrays([2,-7,-6]))

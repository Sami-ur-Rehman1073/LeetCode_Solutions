def threeSum(nums):
    sol = []
    i = 0
    nums.sort()
    print(nums)
    for i in range(len(nums)-2):
        low = i + 1
        high = len(nums) - 1
        if i == 0 or nums[i] != nums[i-1]:
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                if total < 0:
                    low += 1
                elif total > 0:
                    high -= 1
                elif total == 0:
                    sol.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                            low += 1
                    while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                    low += 1
                    high -= 1
    return sol

print(threeSum([-1,0,1,2,-1,-4]))
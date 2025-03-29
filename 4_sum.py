
def fourSum(nums, target):
    nums.sort()
    result = []
    i = 0 
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, len(nums)-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            low = j + 1
            high = len(nums) - 1
            while low < high:
                total = nums[i] + nums[j] + nums[low] + nums[high]
                if total < target:
                    low += 1
                if total > target:
                    high -= 1 
                if total == target:
                    result.append([nums[i], nums[j], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
    return result
                           
print(fourSum([1,0,-1,0,-2,2], 0))


    

    
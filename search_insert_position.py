def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            high = mid - 1 
        
        else:
            low = mid + 1
    return low
    

print(searchInsert([1,3,5,6], 4))
def searchRange(nums, target): 
    if len(nums) == 1:
        return [0, 0]
    result = []
    def findstart(nums):
        first = -1
        low = 0 ; high = len(nums) - 1
        while low <= high:
            mid = (low + high)// 2
            if nums[mid] == target:
                first = mid  
                high = mid - 1                          
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def findend(nums):
        low = 0 ; high = len(nums) - 1
        end = -1
        while low <= high:
            mid = (low + high)// 2
            if nums[mid] == target:
                end = mid
                low = mid + 1               
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        return end 

    result = [findstart(nums), findend(nums)]
    return result

print(searchRange([2, 2], 2))

        
def sortColors(nums):
    nums = nums + [float('inf')]
    def parition(low, high):
        pivot = nums[low]

        i = low ; j = high
        while i < j: 
            while(nums[i] <= pivot):
                i += 1
            while(nums[j] > pivot):
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], nums[low]
        return j
    
    def quick_sort(low, high):
        if low < high:
            j = parition(low, high)
            quick_sort(low, j-1)
            quick_sort(j+1, high)
        return nums
    
    nums = quick_sort(0, len(nums)-1)
    nums = nums[:len(nums)-1]
    return nums
    
print(sortColors([2,0,2,1,1,0]))
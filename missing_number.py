                    # Basic Approach

def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i

print(missingNumber([3,0,1]))




                # by using maths

    
def missingNumber(nums):
    n = len(nums) ; s = sum(nums)
    sum_arithematic_series = (n * (n + 1)) // 2 
    return sum_arithematic_series - s

print(missingNumber([3,0,1]))


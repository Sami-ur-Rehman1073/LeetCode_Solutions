def divideArray(nums):
    if nums == []:
        return False
    vals = set(nums)
    for i in vals:
        if nums.count(i) % 2 != 0:
            return False
    return True

print(divideArray([1,2,3,4]))     
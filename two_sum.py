                                # Solution - 1 #

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]
    

print(two_sum([3, 6, 3], 6))

                                # Solution - 2 #

def two_sum(nums, target):
    for i in range(len(nums)):
        second_num = target - nums[i]
        sub_nums = nums[i+1:len(nums)]
        if second_num in sub_nums:
            index2 = sub_nums.index(second_num) + (i+1)
            return [i, index2]

print(two_sum([3, 6, 3], 6))

                                # Solution - 3 #

def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        second_num = target - nums[i]
        if second_num in seen:
            index2 = nums.index(second_num)
            return [i, index2]
        seen[nums[i]] = i

print(two_sum([3, 6, 3], 6))
 
def intersection(nums1, nums2):
    result = []
    seen = set()

    for i in (nums1):
        if i not in seen:
            if i in nums2:
                result.append(i)
                seen.add(i)
    
    return result

print(intersection([4,9,5], [9,4,9,8,4]))
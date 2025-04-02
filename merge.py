def merge(nums1, m, nums2, n):
    result = []
    i = j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums1[i] == nums2[j]:
            result.append(nums1[i])
            result.append(nums2[j])
            i += 1
            j += 1
        else: 
            result.append(nums2[j])
            j += 1
    
    for p in range(i , m):
        result.append(nums1[p])
    for q in range(j , n):
        result.append(nums2[q])

    nums1 = result
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))  
        
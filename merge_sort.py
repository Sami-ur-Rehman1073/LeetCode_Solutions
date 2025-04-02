def sortArray(nums):

    def merge_sort(arr):

        def merge(left, right):
            result = []
            i = j = 0
            m, n = len(left), len(right)
            while (i < m) and (j < n):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                elif left[i] == right[j]:
                    result.append(left[i])
                    result.append(right[j])
                    i += 1
                    j += 1
                else:
                    result.append(right[j])
                    j += 1
            
            for p in range(i , m):
                result.append(left[p])
            for q in range(j , n):
                result.append(right[q])

            return result
            

        if len(arr) == 1:
            return arr
        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)
    
    return merge_sort(nums)
    

print(sortArray([5,1,1,2,0,0]))
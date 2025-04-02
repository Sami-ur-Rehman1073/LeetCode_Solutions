# by using heaps

import heapq
from collections import Counter
def topKFrequent(nums, k):
    heap = []
    nums_count = Counter(nums)

    for i in nums_count.keys():
        if len(heap) < k:
            heapq.heappush(heap, (nums_count[i] , i))
        else:
            heapq.heappushpop(heap, (nums_count[i] , i))

    return [i[1] for i in heap]

print(topKFrequent([1,1,1,2,2,3], k = 2))

# by using hashmap

from collections import Counter
def topKFrequent(nums, k):
    nums_count = Counter(nums)
    sorted_nums = sorted(nums_count.keys(), key=lambda x: nums_count[x], reverse = True)
    return [sorted_nums[i] for i in range(k)]
print(topKFrequent([1,1,1,2,2,3], k = 2))




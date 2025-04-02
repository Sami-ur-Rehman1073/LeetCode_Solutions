import heapq
def findKthLargest(nums, k):
    for i in range(len(nums)):
        nums[i] = -nums[i]

    heapq.heapify(nums)

    for _ in range(k - 1):
        heapq.heappop(nums)

    return -heapq.heappop(nums)


    
print(findKthLargest([3,2,3,1,2,4,5,5,6]))

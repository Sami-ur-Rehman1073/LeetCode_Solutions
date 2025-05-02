def heightChecker(heights):
    sorted_heights = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            count += 1
    return count

print(heightChecker([1,1,4,2,1,3]))
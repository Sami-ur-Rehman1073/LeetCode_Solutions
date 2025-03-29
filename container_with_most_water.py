def max_capacity(height):
    left = 0
    right = len(height)-1
    max_area = -1
    while left < right:
        length = min(height[left], height[right])
        width = right - left
        area = length * width
        if area > max_area:
            max_area = area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area

print(max_capacity([1,8,6,2,5,4,8,3,7]))
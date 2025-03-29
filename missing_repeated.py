
def findMissingAndRepeatedValues(grid):
    
    n = len(grid) * len(grid[0])
    sum_expected = (n * (n + 1)) // 2
    sum_squared_expected = (n * (n + 1) * ((n * 2)  +  1)) // 6
    
    def sum_finder(grid):
        total_sum = 0
        for i in grid:
            for j in i:
                total_sum += j 
        return total_sum
         
    def squared_sum_finder(grid):
        total_squared_sum = 0
        for i in grid:
            for j in i:
                total_squared_sum += j ** 2
        return total_squared_sum
    
    sum_original = sum_finder(grid)
    sum_squared_original = squared_sum_finder(grid)

    a = sum_expected - sum_original
    b = sum_squared_expected - sum_squared_original

    r = (b - (a ** 2)) // (2 * a)

    m = a + r

    return [r , m]
    
print(findMissingAndRepeatedValues([[1,3],[2,2]]))
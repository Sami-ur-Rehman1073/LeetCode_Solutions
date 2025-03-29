def rotate(matrix):
    def transpose(matrix):
        for i in range(len(matrix)):
            p = matrix[i]
            for j in range(len(p)):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def reverse(matrix):
        trans_matrix = transpose(matrix)
        for i in range(len(trans_matrix)):
            p = trans_matrix[i]
            left = 0
            right = len(p) - 1
            while left < right:
                p[left], p[right] = p[right], p[left]
                left += 1
                right -= 1
        return trans_matrix

    return reverse(matrix)

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
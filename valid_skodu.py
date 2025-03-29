def isValidSudoku(board):

    for i in range(9):
        seen = set()
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in seen:
                    return False
            seen.add(board[i][j])
    

    for i in range(9):
        seen = set()
        for j in range(9):
            if board[j][i] != ".":
                if board[j][i] in seen:
                    return False
            seen.add(board[j][i]) 

    rows = [3, 6, 9]

    hashmap = {(0, 0) : set(),
               (0, 1) : set(),
               (0, 2) : set(),
               (1, 0) : set(),
               (1, 1) : set(),
               (1, 2) : set(),
               (2, 0) : set(),
               (2, 1) : set(),
               (2, 2) : set(),
               }
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in hashmap[(i//3, j//3)]:
                    return False
                hashmap[(i//3, j//3)].add(board[i][j])

    return True
            
        
print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))




        
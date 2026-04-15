def ValidSudoku(board):
    repsCol = []
    repsRaw = []
    
    for i in range(9):
        for j in range(8):
            #check columns
            if board[j][i] != ".":
                repsCol.append(board[j][i])
            if board[j+1][i] in repsCol:
                return False
            
            #check rows
            if board[i][j] != ".":
                repsRaw.append(board[i][j])
            if board[i][j+1] in repsRaw:
                return False
        repsCol.clear()
        repsRaw.clear()
    
    #check 3x3 sub-boxes
    repSubBox = []
    startRow = 0
    endRow = 3
    for row in range(startRow, endRow):
        startCol = 0
        endCol = 3
 
        for col in range(3):
            for i in range(3):
                for j in range(3):
                    if board[startRow:endRow][i][startCol:endCol][j] != ".":
                        repSubBox += board[startRow:endRow][i][startCol:endCol][j]
            if len(set(repSubBox)) < len(repSubBox):
                return False
            repSubBox.clear()
            startCol += 3
            endCol += 3

        startRow += 3
        endRow += 3
    return True

           
print(ValidSudoku([
 ['5','3','.','.','7','.','.','.','.'],
 ['6','.','.','1','9','5','.','.','.'],
 ['.','9','8','.','.','.','.','6','.'],
 ['8','.','.','.','6','.','.','.','3'],
 ['4','.','.','8','.','3','.','.','1'],
 ['7','.','.','.','2','.','.','.','6'],
 ['.','6','.','.','.','.','2','8','.'],
 ['.','.','.','4','1','9','.','.','5'],
 ['.','.','.','.','8','.','.','7','9']]))
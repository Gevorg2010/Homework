def queensPlacement(n):
    board = [[" " for j in range(n)] for i in range(n)]
    res = []
    queensNum = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == " ":
                board[i][j] = "Q"
                queensNum += 1

                #attacked row
                for row in range(n):
                    if board[i][row] == " ":
                        board[i][row] = "#"
                
                #attacked column
                for col in range(n):
                    if board[col][j] == " ":
                        board[col][j] = "#"
                
                #attacked diagonal from top left to bottom right
                x = j
                y = i
                while x > 0 or y > 0:
                    x -= 1
                    y -= 1
                hor = x+1
                ver = y+1
                while ver < n and hor < n:
                    if board[ver][hor] == " ":
                        board[ver][hor] = "#"
                    ver += 1
                    hor += 1

        if queensNum == n:
            res.append(board)
            break
        
    for i in board:
        print(i)


queensPlacement(10)
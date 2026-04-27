maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['o', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', ' '],
        ['#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
direct = ">"

# getting start coordinates
for i in range(len(maze)):
    try:
        startj = maze[i].index("o")
    except Exception:
        continue
    else:
        j = startj
        starti = i
        break

def move(maze, i, j, direct):
    if direct == ">":
        if maze[i+1][j] == " ":
            maze[i+1][j] = "o"; maze[i][j] = " "; direct = "v"; i += 1
        elif maze[i][j+1] == " ":
            maze[i][j+1] = "o"; maze[i][j] = " "; direct = ">"; j += 1
        elif maze[i-1][j] == " ":
            maze[i-1][j] = "o"; maze[i][j] = " "; direct = "^"; i -= 1
        else:
            maze[i][j-1] = "o"; maze[i][j] = " "; direct = "<"; j -= 1
        
    elif direct == "v":
        if maze[i][j-1] == " ":
            maze[i][j-1] = "o"; maze[i][j] = " "; direct = "<"; j -= 1
        elif maze[i+1][j] == " ":
            maze[i+1][j] = "o"; maze[i][j] = " "; direct = "v"; i += 1
        elif maze[i][j+1] == " ":
            maze[i][j+1] = "o"; maze[i][j] = " "; direct = ">"; j += 1
        else:
            maze[i-1][j] = "o"; maze[i][j] = " "; direct = "^"; i -= 1
        
    elif direct == "<":
        if maze[i-1][j] == " ":
            maze[i-1][j] = "o"; maze[i][j] = " "; direct = "^"; i -= 1
        elif maze[i][j-1] == " ":
            maze[i][j-1] = "o"; maze[i][j] = " "; direct = "<"; j -= 1
        elif maze[i+1][j] == " ":
            maze[i+1][j] = "o"; maze[i][j] = " "; direct = "v"; i += 1
        else:
            maze[i][j+1] = "o"; maze[i][j] = " "; direct = ">"; j += 1
    
    else: 
        if maze[i][j+1] == " ":
            maze[i][j+1] = "o"; maze[i][j] = " "; direct = ">"; j += 1
        elif maze[i-1][j] == " ":
            maze[i-1][j] = "o"; maze[i][j] = " "; direct = "^"; i -= 1
        elif maze[i][j-1] == " ":
            maze[i][j-1] = "o"; maze[i][j] = " "; direct = "<"; j -= 1
        else:
            maze[i+1][j] = "o"; maze[i][j] = " "; direct = "v"; i += 1
    
    return i, j, direct

steps = 0
while True:
    for row in maze:
        print(row)
    print("-" * 12) 

    if (i == 0 or i == len(maze)-1 or j == 0 or j == len(maze[0])-1) and steps > 0:
        print("Destination reached!")
        break
    
    if i == starti and j == startj and steps > 0:
        print("No exit!")
        break

    input("Press Enter to countinue")

    i, j, direct = move(maze, i, j, direct)
    steps += 1


board = [ 
   #  0   1   2   3   4   5   6   7
    ['-','2','-','2','-','2','-','2'],#0
    ['2','-','2','-','2','-','2','-'],#1
    ['-','2','-','0','-','2','-','2'],#2
    ['0','-','2','-','0','-','0','-'],#3
    ['-','1','-','0','-','0','-','0'],#4
    ['1','-','1','-','1','-','1','-'],#5
    ['-','1','-','1','-','1','-','1'],#6
    ['1','-','1','-','1','-','1','-'] #7
]

def printBoard():
    for i in range(8):
        for j in range(8):
            print(board[i][j]+ ' ', end='')
        print()
                

def possibleMovesChecker(line:int, collumn:int):
    if line < 8 and collumn < 8 and line >= 0 and collumn >= 0:
        possibleMoves = set()
        if board[line][collumn] == '2':
            if line+1 < 8 and collumn-1 >= 0 and board[line+1][collumn-1] == '0':
                possibleMoves.add((line+1,collumn-1))
            elif line+2 < 8 and collumn-2 >= 0 and board[line+1][collumn-1] != board[line][collumn] and board[line+2][collumn-2] == '0':
                possibleMoves.add((line+2,collumn-2))
            if line+1 < 8 and collumn+1 < 8 and board[line+1][collumn+1] == '0':
                possibleMoves.add((line+1,collumn+1))
            elif line+2 < 8 and collumn+2 < 8 and board[line+1][collumn+1] != board[line][collumn] and board[line+2][collumn+2] == '0':
                possibleMoves.add((line+2,collumn+2))
        else:
            if line-1 >= 0 and collumn-1 >= 0 and board[line-1][collumn-1] == '0':
                possibleMoves.add((line-1,collumn-1))
            elif line-2 >= 0 and collumn-2 >= 0 and board[line-1][collumn-1] != board[line][collumn] and board[line-2][collumn-2] == '0':
                possibleMoves.add((line-2,collumn-2))
            if line-1 >= 0 and collumn+1 < 8 and board[line-1][collumn+1] == '0':
                possibleMoves.add((line-1,collumn+1))
            elif line-2 >= 0 and collumn+2 < 8 and board[line-1][collumn+1] != board[line][collumn] and board[line-2][collumn+2] == '0':
                possibleMoves.add((line-2,collumn+2))
        return possibleMoves         
    return None
              
              
                
printBoard()
print(possibleMovesChecker(4,1))

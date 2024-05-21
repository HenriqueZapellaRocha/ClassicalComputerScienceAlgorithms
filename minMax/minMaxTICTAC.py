#minamax algorithim implemented in a simple tic tac game
import math



board = []

def printBoard() -> None:
    for i in range(9):
        if (i+1) % 3 == 0 and i != 0:
            print(board[i], end='')
            print("\n")
        else:
            print(board[i] + "|", end='')
            
def makeMove(position: int, value:str) -> None:
    if board[position] == ' ':
        board[position] = value


def startBoard():
    for i in range(9):
        board.append(' ')
        
startBoard()

def verifyWinner(value : str):
    if  board[0] == board[1] == board[2] == value:
        return True 
    elif board[3] == board[4] == board[5] == value:
        return True
    elif  board[6] == board[7] == board[8] == value:
        return True
    elif  board[0] == board[1] == board[2] == value:
        return True
    elif board[0] == board[4] == board[8] == value:
        return True
    elif  board[2] ==  board[4] ==  board[6] == value:
        return True
    elif  board[0] ==  board[3] ==  board[6] == value:
        return True
    elif  board[1] ==  board[4] ==  board[7] == value:
        return True
    elif  board[2] ==  board[5] ==  board[8] == value:
        return True
    else:
        return False
    
def verifyIsFull():
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

def minMax(isMaximizing) -> float:
    if verifyWinner('X'):
        return -1
    elif verifyWinner('O'):
        return 1
    elif verifyIsFull():
        return 0
    
    if isMaximizing == True:
        bestScore = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minMax(False)
                board[i] = ' '
                bestScore = max(bestScore, score)
        return bestScore
    
    else:
        bestScore = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minMax(True)
                board[i] = ' '
                bestScore = min(bestScore, score)
        return bestScore
            
def machineMovement():
    bestScore = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minMax(False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                move = i
    
    return move
                
        
printBoard()
while True:

    print('\n')
    makeMove(int(input("enter position:")), 'X')
    printBoard()
    if verifyWinner('X'):
        exit(0)
    if verifyIsFull():
        exit(0)
    makeMove(machineMovement(),'O')
    print("machine make movement")
    printBoard()
    if verifyWinner('O'):
        exit(0)
    if verifyIsFull():
        exit(0)
        

    
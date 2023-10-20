N = int(input("Enter board size : "))

#left diagonal
ld = [0] * 30

#right diagonal
rd = [0] * 30

#row check
cl = [0] * 30

def printSol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

def solveNQ(board, col):
    if (col >= N):
        return True
        
    for i in range(N):
        if ((ld[i - col + N - 1] != 1 and
            rd[i + col] != 1) and cl[i] != 1):
                
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            if (solveNQ(board, col + 1)):
                return True
        
            board[i][col] = 0 # Backtrack
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
            
    return False
    
def solve(s):
    board = [[0 for j in range(s)] for i in range(s)]
    if (solveNQ(board, 0) == False):
        print("No Solution exist")
        return False
    printSol(board)
    return True

solve(N)
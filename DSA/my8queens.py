def is_safe(board,i,j):
    #left row check:
    for k in range(j):
        if board[i][k]==1:
            return False
    #upside diagonal check:
    for k,l in zip(range(i,-1,-1),range(j,-1,-1)):
        if board[k][l]==1:
            return False
    #downside diagonal check:
    for k,l in zip(range(i,len(board),1),range(j,-1,-1)):
        if board[k][l]==1:
            return False
    return True
def arranging(board,col):
    #base case
    if col>=len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board,i,col):
            board[i][col]=1
            if arranging(board,col+1):
                return True
            board[i][col]=0
    return False
#board=[[0]*8]*8 only takes shallow copy so change in one list will reflect in all the other list.
board=[[0]*8 for i in range(8)]
arranging(board,0)
for i in board:
    print(i)
    

def solve():
    N = 8
    board = [[0] * N for _ in range(N)]
    if not arranging(board, 0):
        print("Solution does not exist")
        return False
    for i in board:
        print(i)

    
    return True

#solve()
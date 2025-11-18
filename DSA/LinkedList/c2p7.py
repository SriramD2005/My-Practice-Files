#path finding problem
def inmat(mat,i,j):
    n=len(mat)
    return i<n and j<n
def pathfinder(mat,i,j,n):
    global path
    if i==n and j==n:
        path.append((i,j))
        return True
    elif mat[i][j]==1 and inmat(mat,i,j):
        path.append((i,j))
        if pathfinder(mat,i,j+1,n):
            return True
        if pathfinder(mat,i+1,j,n):
            return True
        path.pop()
        return False
    return False
path=[]
mat=[[1,1,1,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,0,0],[1,1,1,1,1]]
pathfinder(mat,0,0,4)
print(path)

        
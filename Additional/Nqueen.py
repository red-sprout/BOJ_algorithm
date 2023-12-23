def dfs(row):
    global ANS
    if(row == N):
        ANS += 1
        return
    
    for col in range(N):
        if(isValid(row, col)):
            column[row] = col
            visited[col] = True
            dfs(row + 1)
            visited[col] = False
    
def isValid(row, col):
    if(visited[col]):
        return False
    
    for oldRow in range(row):
        oldCol = column[oldRow]
        if(abs(row - oldRow) == abs(col - oldCol)):
            return False
    
    return True


N = int(input())
ANS = 0

column = [0 for i in range(N)]
visited = [False for i in range(N)]

dfs(0)

print(ANS)
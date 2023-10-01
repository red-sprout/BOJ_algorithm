N, M = map(int, input().split())
arr = []

def dfs(idx):
    global arr
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(idx, N + 1):
        idx = i
        if i not in arr:
            arr.append(i)
            dfs(idx + 1)
            arr.pop()

dfs(1)
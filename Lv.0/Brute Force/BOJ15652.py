N, M = map(int, input().split())
arr = []

def dfs(idx):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, N + 1):
        idx = i
        arr.append(idx)
        dfs(idx)
        arr.pop()

dfs(1)
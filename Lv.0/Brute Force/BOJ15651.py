N, M = map(int,input().split())
arr = []

def dfs():
    global arr
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    else:
        for i in range(1, N + 1):
            arr.append(i)
            dfs()
            arr.pop()

dfs()
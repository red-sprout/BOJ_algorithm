def one(arr, N, M):
    result = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            result[i][j] = arr[N - 1 - i][j]
    return result

def two(arr, N, M):
    result = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            result[i][j] = arr[i][M - 1 - j]
    return result

def three(arr, N, M):
    result = [[0 for i in range(N)] for j in range(M)]
    for i in range(N):
        for j in range(M):
            result[j][i] = arr[N - 1 - i][j]
    return result

def four(arr, N, M):
    result = [[0 for i in range(N)] for j in range(M)]
    for i in range(N):
        for j in range(M):
            result[j][i] = arr[i][M - 1 - j]
    return result

def five(arr, N, M):
    result = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if i < N//2 and j < M//2:
                result[i][j + M//2] = arr[i][j]
            elif i < N//2 and j >= M//2:
                result[i + N//2][j] = arr[i][j]
            elif i >= N//2 and j >= M//2:
                result[i][j - M//2] = arr[i][j]
            else:
                result[i - N//2][j] = arr[i][j]
    return result

def six(arr, N, M):
    result = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if i < N//2 and j < M//2:
                result[i + N//2][j] = arr[i][j]
            elif i < N//2 and j >= M//2:
                result[i][j - M//2] = arr[i][j]
            elif i >= N//2 and j >= M//2:
                result[i - N//2][j] = arr[i][j]
            else:
                result[i][j + M//2] = arr[i][j]
    return result

N, M, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
cal = list(map(int, input().split()))

for num in cal:
    N, M = len(arr), len(arr[0])
    if num == 1:
        arr = one(arr, N, M)
    elif num == 2:
        arr = two(arr, N, M)
    elif num == 3:
        arr = three(arr, N, M)
    elif num == 4:
        arr = four(arr, N, M)
    elif num == 5:
        arr = five(arr, N, M)
    else:
        arr = six(arr, N, M)

for row in arr:
    print(*row)
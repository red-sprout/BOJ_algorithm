N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if j == 0:
            if i == 0:
                continue
            else:
                arr[i][j] += arr[i-1][j]
        else:
            if i == 0:
                arr[i][j] += arr[i][j-1]
                continue
            else:
                arr[i][j] += max(arr[i-1][j], arr[i][j-1],arr[i-1][j-1])

print(arr[N-1][M-1])
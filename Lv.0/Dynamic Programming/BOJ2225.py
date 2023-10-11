CONST = 1000000000
N, K = map(int,input().split())
DP = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(1, K + 1):
    for j in range(N + 1):
        if j == 0:
            DP[i][j] = 1
            continue
        else:
            DP[i][j] = (DP[i][j - 1] + DP[i - 1][j]) % CONST
print(DP[K][N])
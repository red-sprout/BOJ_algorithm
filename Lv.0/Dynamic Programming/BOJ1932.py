N = int(input())
DP = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    if i == 0:
        DP[0][0] = int(input())
        continue
    tmp = list(map(int,input().split()))
    for j in range(i + 1):
        if j == 0:
            DP[i][j] = tmp[j] + DP[i-1][j]
        elif j == i:
            DP[i][j] = tmp[j] + DP[i-1][j-1]
        else:
            DP[i][j] = tmp[j] + max(DP[i-1][j], DP[i-1][j-1])
print(max(DP[N-1]))
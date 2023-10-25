T = int(input())
for _ in range(T):
    n = int(input())
    row_1 = list(map(int,input().split()))
    row_2 = list(map(int,input().split()))
    row = [row_1, row_2]
    DP = [[0, 0] for i in range(n)]
    DP[0][0], DP[0][1] = row[0][0], row[1][0]
    if n > 1:
        DP[1][0], DP[1][1] = DP[0][1] + row[0][1], DP[0][0] + row[1][1]
    for i in range(2, n):
        DP[i][0] = max(DP[i-1][1] + row[0][i], max(DP[i-2]) + row[0][i])
        DP[i][1] = max(DP[i-1][0] + row[1][i], max(DP[i-2]) + row[1][i])
    print(max(DP[n-1]))
n = int(input())
arr = list(map(int,input().split()))
DP = [[i for i in arr] for j in range(2)]
for i in range(1, n):
    DP[0][i] = max(DP[0][i], DP[0][i-1] + DP[0][i])
    DP[1][i] = max(DP[0][i-1], DP[1][i-1] + arr[i])
print(max(max(DP[0]), max(DP[1])))